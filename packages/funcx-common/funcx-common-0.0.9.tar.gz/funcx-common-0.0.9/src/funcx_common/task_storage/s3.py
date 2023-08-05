import typing as t

try:
    import boto3
    import botocore.exceptions

    has_boto3 = True
except ImportError:
    has_boto3 = False

from ..tasks import TaskProtocol
from .base import StorageException, TaskStorage


class RedisS3Storage(TaskStorage):
    """
    Abstract storage over Redis and S3.
    Uses Redis to store objects below of size threshold, and S3 for the rest
    """

    def __init__(self, bucket_name: str, redis_threshold: int = 20000) -> None:
        """
        :param bucket_name: Name of the S3 bucket to use
        :param redis_threshold: Max size(chars) of the data that redis accommodates
        """

        if not has_boto3:
            raise RuntimeError(
                "Cannot construct RedisS3Storage object since the boto3"
                "package is not available. Either install it explicitly or install the "
                "'boto3' extra, as in\n"
                "  pip install 'funcx-common[boto3]'"
            )

        self.bucket_name = bucket_name
        self.client = boto3.client("s3")
        self.redis_threshold = redis_threshold

    def _store_to_s3(self, task: TaskProtocol, result: str) -> None:
        key = f"{task.task_id}.result"
        try:
            self.client.put_object(
                Body=result.encode("utf-8"),
                Bucket=self.bucket_name,
                Key=key,
            )
        except botocore.exceptions.ClientError as err:
            raise StorageException(
                f"Putting result into s3 for task:{task.task_id} failed"
            ) from err
        else:
            task.result_reference = {
                "storage_id": "s3",
                "s3bucket": self.bucket_name,
                "key": key,
            }

    def _get_from_s3(self, task: TaskProtocol) -> str:
        assert task.result_reference
        try:
            response = self.client.get_object(
                Bucket=task.result_reference["s3bucket"],
                Key=task.result_reference["key"],
            )
            body = response["Body"]
            return t.cast(str, body.read().decode("utf-8"))
        except botocore.exceptions.ClientError as err:
            raise StorageException(
                f"Fetching object from S3 failed for: {task.task_id}"
            ) from err

    def store_result(
        self,
        task: TaskProtocol,
        result: str,
    ) -> None:
        if len(result) > self.redis_threshold:
            # Task is too big for Redis, store in S3
            self._store_to_s3(task, result)
        else:
            task.result = result
            task.result_reference = {"storage_id": "redis"}

    def get_result(self, task: TaskProtocol) -> t.Optional[str]:
        """

        :param task:
        :return: Results result if available, else returns None
        Raises StorageException if fetching fails
        """
        # We should be able to safely remove the following block
        # once all tasks launched with v0.3.3 and prior have TTL'ed out
        if task.result:
            return task.result

        if task.result_reference:
            if task.result_reference["storage_id"] == "s3":
                return self._get_from_s3(task)

            # The following is redundant now while the block above
            # for backward compat exists
            elif task.result_reference["storage_id"] == "redis":
                return task.result
            else:
                raise StorageException(
                    f"Unknown Storage requested: {task.result_reference}"
                )
        else:
            return None
