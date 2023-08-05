# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raclients', 'raclients.graph', 'raclients.lora', 'raclients.mo']

package_data = \
{'': ['*']}

install_requires = \
['Authlib>=0.15.5,<0.16.0',
 'aiohttp>=3.7.4,<4.0.0',
 'fastapi>=0.70.0,<0.71.0',
 'gql',
 'httpx>=0.20.0,<0.21.0',
 'jsonschema>=3.2.0,<4.0.0',
 'more-itertools>=8.7.0,<9.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'ra-utils[headers]>=0.4.0,<0.5.0',
 'ramodels>=3.0.0,<4.0.0',
 'respx>=0.18.2,<0.19.0',
 'structlog>=21.2.0,<22.0.0',
 'tqdm>=4.60.0,<5.0.0']

setup_kwargs = {
    'name': 'raclients',
    'version': '0.7.2',
    'description': 'Clients for OS2mo/LoRa',
    'long_description': '<!--\nSPDX-FileCopyrightText: 2021 Magenta ApS <https://magenta.dk>\nSPDX-License-Identifier: MPL-2.0\n-->\n\n\n# RA Clients\n\nOS2mo/LoRa clients\n\n<!--\n## Versioning\nThis project uses [Semantic Versioning](https://semver.org/) with the following strategy:\n- MAJOR: Incompatible changes to existing data models\n- MINOR: Backwards compatible updates to existing data models OR new models added\n- PATCH: Backwards compatible bug fixes\n\n## Getting Started\n\nTODO: README section missing!\n\n### Prerequisites\n\n\nTODO: README section missing!\n\n### Installing\n\nTODO: README section missing!\n\n## Running the tests\n\nTODO: README section missing!\n\n## Deployment\n\nTODO: README section missing!\n\n## Built With\n\nTODO: README section missing!\n\n## Authors\n\nMagenta ApS <https://magenta.dk>\n\nTODO: README section missing!\n-->\n## License\n- This project: [MPL-2.0](MPL-2.0.txt)\n- Dependencies:\n  - pydantic: [MIT](MIT.txt)\n\nThis project uses [REUSE](https://reuse.software) for licensing. All licenses can be found in the [LICENSES folder](LICENSES/) of the project.\n',
    'author': 'Magenta',
    'author_email': 'info@magenta.dk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://magenta.dk/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
