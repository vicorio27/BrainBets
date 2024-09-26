import datetime
import boto3

from boto3.s3.transfer import ClientError

s3_resource = boto3.resource("s3")


def hello_s3():
    """
    Use the AWS SDK for Python (Boto3) to create an Amazon Simple Storage Service
    (Amazon S3) resource and list the buckets in your account.
    This example uses the default settings specified in your shared credentials
    and config files.
    """
    print("Hello, Amazon S3! Let's list your buckets:")
    for bucket in s3_resource.buckets.all():
        print(f"\t{bucket.name}")


class ObjectWrapper:
    """Encapsulates S3 object actions."""

    def __init__(self, s3_object):
        """
        :param s3_object: A Boto3 Object resource. This is a high-level resource in Boto3
                          that wraps object actions in a class-like structure.
        """
        self.object = s3_object
        self.key = self.object.key

    def copy(self, dest_object):
        """
        Copies the object to another bucket.

        :param dest_object: The destination object initialized with a bucket and key.
                            This is a Boto3 Object resource.
        """
        try:
            dest_object.copy_from(
                CopySource={"Bucket": self.object.bucket_name, "Key": self.object.key}
            )
            dest_object.wait_until_exists()
            print(
                f"Copied object from %s:%s to %s:%s.",
                self.object.bucket_name,
                self.object.key,
                dest_object.bucket_name,
                dest_object.key,
            )
        except ClientError:
            print(
                f"Couldn't copy object from %s/%s to %s/%s.",
                self.object.bucket_name,
                self.object.key,
                dest_object.bucket_name,
                dest_object.key,
            )
            raise


def create_bucket():
    response = s3_resource.create_bucket(
        ACL="private" | "public-read" | "public-read-write" | "authenticated-read",
        Bucket="string",
        CreateBucketConfiguration={
            "LocationConstraint": "af-south-1"
            | "ap-east-1"
            | "ap-northeast-1"
            | "ap-northeast-2"
            | "ap-northeast-3"
            | "ap-south-1"
            | "ap-south-2"
            | "ap-southeast-1"
            | "ap-southeast-2"
            | "ap-southeast-3"
            | "ca-central-1"
            | "cn-north-1"
            | "cn-northwest-1"
            | "EU"
            | "eu-central-1"
            | "eu-north-1"
            | "eu-south-1"
            | "eu-south-2"
            | "eu-west-1"
            | "eu-west-2"
            | "eu-west-3"
            | "me-south-1"
            | "sa-east-1"
            | "us-east-2"
            | "us-gov-east-1"
            | "us-gov-west-1"
            | "us-west-1"
            | "us-west-2",
            "Location": {"Type": "AvailabilityZone", "Name": "string"},
            "Bucket": {"DataRedundancy": "SingleAvailabilityZone", "Type": "Directory"},
        },
        GrantFullControl="string",
        GrantRead="string",
        GrantReadACP="string",
        GrantWrite="string",
        GrantWriteACP="string",
        ObjectLockEnabledForBucket=True | False,
        ObjectOwnership="BucketOwnerPreferred" | "ObjectWriter" | "BucketOwnerEnforced",
    )


def get_object():
    response = s3_resource.get_object(
        Bucket="string",
        IfMatch="string",
        IfModifiedSince=datetime(2015, 1, 1),
        IfNoneMatch="string",
        IfUnmodifiedSince=datetime(2015, 1, 1),
        Key="string",
        Range="string",
        ResponseCacheControl="string",
        ResponseContentDisposition="string",
        ResponseContentEncoding="string",
        ResponseContentLanguage="string",
        ResponseContentType="string",
        ResponseExpires=datetime(2015, 1, 1),
        VersionId="string",
        SSECustomerAlgorithm="string",
        SSECustomerKey="string",
        RequestPayer="requester",
        PartNumber=123,
        ExpectedBucketOwner="string",
        ChecksumMode="ENABLED",
    )


def list_objects_v2():
    response = s3_resource.list_objects_v2(
        Bucket="string",
        Delimiter="string",
        EncodingType="url",
        MaxKeys=123,
        Prefix="string",
        ContinuationToken="string",
        FetchOwner=True | False,
        StartAfter="string",
        RequestPayer="requester",
        ExpectedBucketOwner="string",
        OptionalObjectAttributes=[
            "RestoreStatus",
        ],
    )


def put_object():
    response = set.put_object(
        ACL="private"
        | "public-read"
        | "public-read-write"
        | "authenticated-read"
        | "aws-exec-read"
        | "bucket-owner-read"
        | "bucket-owner-full-control",
        Body=b"bytes" | "file",
        Bucket="string",
        CacheControl="string",
        ContentDisposition="string",
        ContentEncoding="string",
        ContentLanguage="string",
        ContentLength=123,
        ContentMD5="string",
        ContentType="string",
        ChecksumAlgorithm="CRC32" | "CRC32C" | "SHA1" | "SHA256",
        ChecksumCRC32="string",
        ChecksumCRC32C="string",
        ChecksumSHA1="string",
        ChecksumSHA256="string",
        Expires=datetime(2015, 1, 1),
        IfNoneMatch="string",
        GrantFullControl="string",
        GrantRead="string",
        GrantReadACP="string",
        GrantWriteACP="string",
        Key="string",
        Metadata={"string": "string"},
        ServerSideEncryption="AES256" | "aws:kms" | "aws:kms:dsse",
        StorageClass="STANDARD"
        | "REDUCED_REDUNDANCY"
        | "STANDARD_IA"
        | "ONEZONE_IA"
        | "INTELLIGENT_TIERING"
        | "GLACIER"
        | "DEEP_ARCHIVE"
        | "OUTPOSTS"
        | "GLACIER_IR"
        | "SNOW"
        | "EXPRESS_ONEZONE",
        WebsiteRedirectLocation="string",
        SSECustomerAlgorithm="string",
        SSECustomerKey="string",
        SSEKMSKeyId="string",
        SSEKMSEncryptionContext="string",
        BucketKeyEnabled=True | False,
        RequestPayer="requester",
        Tagging="string",
        ObjectLockMode="GOVERNANCE" | "COMPLIANCE",
        ObjectLockRetainUntilDate=datetime(2015, 1, 1),
        ObjectLockLegalHoldStatus="ON" | "OFF",
        ExpectedBucketOwner="string",
    )
