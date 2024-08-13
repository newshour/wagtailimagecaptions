import hashlib
import logging
from os.path import basename

from django.core.files.images import ImageFile
from PIL import Image as PILImage
from PIL.IptcImagePlugin import getiptcinfo
from wagtail.images import get_image_model

logger = logging.getLogger(__name__)


def imagefile_to_model(image_file: ImageFile):
    """
    Converts an ImageFile to our image model.
    """
    ImageModel = get_image_model()

    with image_file.open(mode="rb") as f:
        file_hash = hashlib.sha1(f.read()).hexdigest()

        try:
            image, created = ImageModel.objects.get_or_create(
                file_hash=file_hash,
                defaults={"title": basename(image_file.name), "file": image_file},
            )
            return image
        except ImageModel.MultipleObjectsReturned:
            logger.error(
                "Multiple versions of %s (%s) found. Returning the first one found.",
                basename(image_file.name),
                file_hash,
            )
            return ImageModel.objects.filter(file_hash=file_hash).first()


def parse_iptc(image_file: ImageFile) -> dict:
    """
    Extracts IPTC data from an image (tiff, jpeg). For more inforation see:
        https://www.iptc.org/std/IIM/3.0/specification/IIMV3.PDF
    """
    try:
        image = PILImage.open(image_file)
        iptc = getiptcinfo(image)
    except FileNotFoundError as fnfe:
        logger.warning(fnfe)
        return {}
    except ValueError as ve:
        logger.warning(ve)
        return {}

    iptc_dict = {}

    if not iptc:
        logger.info("Image did not contain IPTC data.")
        return iptc_dict

    def decode(v):
        if isinstance(v, bytes):
            return bytes.decode(v)
        elif isinstance(v, list):
            return [decode(item) for item in v]
        elif isinstance(v, str):
            return v

    # fmt: off
    for k, v in iptc.items():
        if k == (2, 5,):
            iptc_dict["object_name"] = decode(v)
        elif k == (2, 7,):
            iptc_dict["edit_status"] = decode(v)
        elif k == (2, 25,):
            iptc_dict["keywords"] = decode(v)
        elif k == (2, 30,):
            iptc_dict["release_date"] = decode(v)
        elif k == (2, 35,):
            iptc_dict["release_time"] = decode(v)
        elif k == (2, 37,):
            iptc_dict["expiration_date"] = decode(v)
        elif k == (2, 38,):
            iptc_dict["expiration_time"] = decode(v)
        elif k == (2, 40,):
            iptc_dict["instructions"] = decode(v)
        elif k == (2, 40,):
            iptc_dict["instructions"] = decode(v)
        elif k == (2, 42,):
            iptc_dict["action_advised"] = decode(v)
        elif k == (2, 80,):
            iptc_dict["byline"] = decode(v)
        elif k == (2, 85,):
            iptc_dict["byline_title"] = decode(v)
        elif k == (2, 90,):
            iptc_dict["city"] = decode(v)
        elif k == (2, 92,):
            iptc_dict["sub_location"] = decode(v)
        elif k == (2, 95,):
            iptc_dict["province_state"] = decode(v)
        elif k == (2, 100,):
            iptc_dict["country"] = decode(v)
        elif k == (2, 105,):
            iptc_dict["headline"] = decode(v)
        elif k == (2, 110,):
            iptc_dict["credit"] = decode(v)
        elif k == (2, 116,):
            iptc_dict["copyright_notice"] = decode(v)
        elif k == (2, 120,):
            iptc_dict["caption"] = decode(v)
        elif k == (2, 122,):
            iptc_dict["writer_editor"] = decode(v)
    # fmt: on

    return {k: v for k, v in iptc_dict.items() if v}
