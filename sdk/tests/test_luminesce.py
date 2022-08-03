import unittest
import logging
import os

import luminesce
from luminesce import CurrentTableFieldCatalogApi
from fbnsdkutilities import ApiClientFactory

class LuminesceTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        if os.getenv("FBN_ACCESS_TOKEN", None) is not None:
            cls.api_factory = ApiClientFactory(luminesce, token=os.environ.get("FBN_ACCESS_TOKEN"))
        else:
            cls.api_factory = ApiClientFactory(luminesce, api_secrets_filename="secrets.json")

        cls.api = cls.api_factory.build(luminesce.api.CurrentTableFieldCatalogApi)

    def test_metadata(self):

        response = self.api.get_catalog()
        self.assertGreaterEqual(len(response), 0, response)


if __name__ == '__main__':
    unittest.main()
