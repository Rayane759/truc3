# [5.4.0](https://gitlab.com/to-be-continuous/maven/compare/5.3.2...5.4.0) (2026-03-29)


### Bug Fixes

* **unscope_vars:** replace glob pattern matching with regex matching ([3dd976c](https://gitlab.com/to-be-continuous/maven/commit/3dd976c53ae0ab1fb043392517e17b867df15726))


### Features

* support CA certs provided as file ([cbf2de8](https://gitlab.com/to-be-continuous/maven/commit/cbf2de8e1ebcb2bcf66c047fe38503b12a092eb9))

## [5.3.2](https://gitlab.com/to-be-continuous/maven/compare/5.3.1...5.3.2) (2026-03-09)


### Bug Fixes

* **sonar:** broken indentation ([b0a5082](https://gitlab.com/to-be-continuous/maven/commit/b0a50824522779f47264098a0675e1d9c0806c43))

## [5.3.1](https://gitlab.com/to-be-continuous/maven/compare/5.3.0...5.3.1) (2026-03-05)


### Bug Fixes

* **sonar:** fix SonarQube API call on tag analysis ([2d5c990](https://gitlab.com/to-be-continuous/maven/commit/2d5c990bf939cfb3b827621c5afb618620f16b98))

# [5.3.0](https://gitlab.com/to-be-continuous/maven/compare/5.2.5...5.3.0) (2026-02-25)


### Features

* **sonar:** export list of vulnerabilities as GitLab report ([6192ac6](https://gitlab.com/to-be-continuous/maven/commit/6192ac6043d0754da0ad62d321fd6a079aba8fc6))

## [5.2.5](https://gitlab.com/to-be-continuous/maven/compare/5.2.4...5.2.5) (2026-02-02)


### Bug Fixes

* replace image tag when registry has a port ([ce57db4](https://gitlab.com/to-be-continuous/maven/commit/ce57db48dff3b72ea045e6df794bc32ab1823857))

## [5.2.4](https://gitlab.com/to-be-continuous/maven/compare/5.2.3...5.2.4) (2026-01-12)


### Bug Fixes

* support dotenv for non-root images ([85f5501](https://gitlab.com/to-be-continuous/maven/commit/85f5501cf909d2fc60bcb4f074c31ff82a72dde0))

## [5.2.3](https://gitlab.com/to-be-continuous/maven/compare/5.2.2...5.2.3) (2026-01-06)


### Bug Fixes

* **bash mode:** unmask errors in shell pipelines with 'set -o pipefail' ([0992d5b](https://gitlab.com/to-be-continuous/maven/commit/0992d5b2396ea3d61543c430b965fa72065ffd6a))

## [5.2.2](https://gitlab.com/to-be-continuous/maven/compare/5.2.1...5.2.2) (2025-12-24)


### Bug Fixes

* non-blocking warning in case failed decoding [@url](https://gitlab.com/url)@ variable ([64b6f20](https://gitlab.com/to-be-continuous/maven/commit/64b6f20d6db0eac20e78f9c158cac0e62b6328e4))

## [5.2.1](https://gitlab.com/to-be-continuous/maven/compare/5.2.0...5.2.1) (2025-11-24)


### Bug Fixes

* use fullname for sonar plugin ([882a8be](https://gitlab.com/to-be-continuous/maven/commit/882a8bedbab4d517f92b3fd630e47d5b1a584bb4))

# [5.2.0](https://gitlab.com/to-be-continuous/maven/compare/5.1.1...5.2.0) (2025-09-30)


### Features

* **release:** support Git commit signing and custom Git user name and email ([ad7aeb0](https://gitlab.com/to-be-continuous/maven/commit/ad7aeb0dc89d30f9f0dcdd52764037849e0f168a))

## [5.1.1](https://gitlab.com/to-be-continuous/maven/compare/5.1.0...5.1.1) (2025-08-26)


### Bug Fixes

* **vault:** avoid nested variable for id_token ([525de01](https://gitlab.com/to-be-continuous/maven/commit/525de01f65e89955e88d456dd3a8a47e2f48a309))

# [5.1.0](https://gitlab.com/to-be-continuous/maven/compare/5.0.0...5.1.0) (2025-08-18)


### Features

* trivy codequality report ([dacc5f0](https://gitlab.com/to-be-continuous/maven/commit/dacc5f089c5b998be04c909b43883307bbdb1384))

# [5.0.0](https://gitlab.com/to-be-continuous/maven/compare/4.5.0...5.0.0) (2025-08-13)


* feat(vault)!: enable certificate verification ([adc9f86](https://gitlab.com/to-be-continuous/maven/commit/adc9f86a7e41f211f2c23a94609de63563832223))


### BREAKING CHANGES

* self-signed certificates must be declared in your GitLab DEFAULT_CA_CERTS or with VAULT_CA_CERTS variable

# [4.5.0](https://gitlab.com/to-be-continuous/maven/compare/4.4.2...4.5.0) (2025-08-12)


### Features

* modular workflow rules ([9df1b5b](https://gitlab.com/to-be-continuous/maven/commit/9df1b5b3ae6136faa0da13b80f7afc559b364e12))

## [4.4.2](https://gitlab.com/to-be-continuous/maven/compare/4.4.1...4.4.2) (2025-08-08)


### Bug Fixes

* cache key for trivy ([189cdb7](https://gitlab.com/to-be-continuous/maven/commit/189cdb7e6920c68adcc4e4ce78244424e316d5a1))

## [4.4.1](https://gitlab.com/to-be-continuous/maven/compare/4.4.0...4.4.1) (2025-08-02)


### Bug Fixes

* **release:** add resource_group to prevent releases in parallel ([c25e655](https://gitlab.com/to-be-continuous/maven/commit/c25e65504d5cc5f85580e8289b76491ab18e8b8b))

# [4.4.0](https://gitlab.com/to-be-continuous/maven/compare/4.3.6...4.4.0) (2025-07-25)


### Features

* configurable [@url](https://gitlab.com/url)@ timeout ([825cae2](https://gitlab.com/to-be-continuous/maven/commit/825cae249041aa309afcb63376df7777bdbd91b6))

## [4.3.6](https://gitlab.com/to-be-continuous/maven/compare/4.3.5...4.3.6) (2025-07-05)


### Bug Fixes

* fix unscope_variables ([b603c73](https://gitlab.com/to-be-continuous/maven/commit/b603c736da90e2fe2bcc5a45ff4a89b3a340c327))

## [4.3.5](https://gitlab.com/to-be-continuous/maven/compare/4.3.4...4.3.5) (2025-07-05)


### Bug Fixes

* **trivy:** disable telemetry and version check ([3627b5e](https://gitlab.com/to-be-continuous/maven/commit/3627b5ee56f032ab46f402ee39070bcb3b3e925d))

## [4.3.4](https://gitlab.com/to-be-continuous/maven/compare/4.3.3...4.3.4) (2025-06-20)


### Bug Fixes

* **skopeo:** use official image ([defcc34](https://gitlab.com/to-be-continuous/maven/commit/defcc34b70d3a2e283c91220208433797f6afa1d))

## [4.3.3](https://gitlab.com/to-be-continuous/maven/compare/4.3.2...4.3.3) (2025-06-20)


### Bug Fixes

* **release:** fix RELEASE_REF regex ([be4fe10](https://gitlab.com/to-be-continuous/maven/commit/be4fe10a79265ded3b400752dd4ca52bc59708f3))

## [4.3.2](https://gitlab.com/to-be-continuous/maven/compare/4.3.1...4.3.2) (2025-06-13)


### Bug Fixes

* replace deprecated Docker Hub registry FQDN ([8e775dc](https://gitlab.com/to-be-continuous/maven/commit/8e775dce43d06ca249949d9bd03c47434cf00586))

## [4.3.1](https://gitlab.com/to-be-continuous/maven/compare/4.3.0...4.3.1) (2025-01-31)


### Bug Fixes

* **sbom:** only generate SBOMs on prod branches, integ branches and release tags ([88eb63d](https://gitlab.com/to-be-continuous/maven/commit/88eb63d5cfcf910eac98d2b0c5edbde72a6b5873))

# [4.3.0](https://gitlab.com/to-be-continuous/maven/compare/4.2.0...4.3.0) (2025-01-28)


### Features

* add vault variant ([a80ac30](https://gitlab.com/to-be-continuous/maven/commit/a80ac3067498bfb9aea04860ee6c839bc0ab7620))

# [4.2.0](https://gitlab.com/to-be-continuous/maven/compare/4.1.0...4.2.0) (2025-01-27)


### Features

* disable tracking service by default ([965198b](https://gitlab.com/to-be-continuous/maven/commit/965198bcd45fe574843222bb919b3ccb62795a40))

# [4.1.0](https://gitlab.com/to-be-continuous/maven/compare/4.0.2...4.1.0) (2025-01-20)


### Features

* **JaCoCo:** add JaCoCo Coverage Reports integration ([1f997a1](https://gitlab.com/to-be-continuous/maven/commit/1f997a18c61d7eb4fe8b9af1ee828893ec70929b))

## [4.0.2](https://gitlab.com/to-be-continuous/maven/compare/4.0.1...4.0.2) (2024-12-29)


### Bug Fixes

* use --pkg-types instead of deprecated --vuln-type ([131a821](https://gitlab.com/to-be-continuous/maven/commit/131a821501a6140f9726fa75beb7e18f2c5f5d6f))

## [4.0.1](https://gitlab.com/to-be-continuous/maven/compare/4.0.0...4.0.1) (2024-12-10)


### Bug Fixes

* add Git branch slug in SNAPSHOT versions for Merge Request ([afcc0b0](https://gitlab.com/to-be-continuous/maven/commit/afcc0b0ccbc09118264412e3075ee8003bcb1dbc))

# [4.0.0](https://gitlab.com/to-be-continuous/maven/compare/3.11.4...4.0.0) (2024-11-26)


### Code Refactoring

* **jib/trivy:** enforce usage of Trivy environment variables ([e62f19e](https://gitlab.com/to-be-continuous/maven/commit/e62f19e98367595b58f07d9275371f75697dc33c))


### BREAKING CHANGES

* **jib/trivy:** 2 Trivy configuration params removed in favor of the native Trivy environment variables

## [3.11.4](https://gitlab.com/to-be-continuous/maven/compare/3.11.3...3.11.4) (2024-10-24)


### Bug Fixes

* set trivy artifact expiration ([fe96b4a](https://gitlab.com/to-be-continuous/maven/commit/fe96b4ae9b2bff3fe803e5aa47ff670c6eccd38f))

## [3.11.3](https://gitlab.com/to-be-continuous/maven/compare/3.11.2...3.11.3) (2024-10-04)


### Bug Fixes

* **release:** support full semantic-versioning specifcation (with prerelease and build metadata) ([3d627c0](https://gitlab.com/to-be-continuous/maven/commit/3d627c0a462e898b4502c515e59b38efc14ee499))

## [3.11.2](https://gitlab.com/to-be-continuous/maven/compare/3.11.1...3.11.2) (2024-09-10)


### Bug Fixes

* Add fail function. fixes [#67](https://gitlab.com/to-be-continuous/maven/issues/67) ([31c979c](https://gitlab.com/to-be-continuous/maven/commit/31c979caece4f247b34477e6cab37158ea29eae4))

## [3.11.1](https://gitlab.com/to-be-continuous/maven/compare/3.11.0...3.11.1) (2024-07-15)


### Bug Fixes

* **jib:** correct the artifacts paths and reports definition ([bbde711](https://gitlab.com/to-be-continuous/maven/commit/bbde711e6d8566ee93da393c35bcfb3fdd0c5a2d)), closes [#62](https://gitlab.com/to-be-continuous/maven/issues/62)

# [3.11.0](https://gitlab.com/to-be-continuous/maven/compare/3.10.2...3.11.0) (2024-07-10)


### Features

* **sbom:** update default SBOM options to include Java catalogers when using the Jib variant ([eb23b26](https://gitlab.com/to-be-continuous/maven/commit/eb23b2608632216d09f949234f18a507028bcf42))

## [3.10.2](https://gitlab.com/to-be-continuous/maven/compare/3.10.1...3.10.2) (2024-07-06)


### Bug Fixes

* replace `packages` by `scan` command ([51dc6c9](https://gitlab.com/to-be-continuous/maven/commit/51dc6c990ab1158adb3fe0763768eab78f7fb406))

## [3.10.1](https://gitlab.com/to-be-continuous/maven/compare/3.10.0...3.10.1) (2024-07-01)


### Bug Fixes

* **Jib:** Trivy 0.53.0 added the clean subcommand for semantic cache management ([6333e64](https://gitlab.com/to-be-continuous/maven/commit/6333e64e61fb025ce758cdb275a6888d934b878b))

# [3.10.0](https://gitlab.com/to-be-continuous/maven/compare/3.9.2...3.10.0) (2024-06-30)


### Bug Fixes

* add submodule pom files as job artifacts ([e6960e6](https://gitlab.com/to-be-continuous/maven/commit/e6960e6b26be9fecb4ce69d38e12919a886132a0))


### Features

* add eval_all_secrets closes [#59](https://gitlab.com/to-be-continuous/maven/issues/59) ([c77193c](https://gitlab.com/to-be-continuous/maven/commit/c77193c447fa897563b07ec0cc5a17ea02e229b8))

## [3.9.2](https://gitlab.com/to-be-continuous/maven/compare/3.9.1...3.9.2) (2024-05-05)


### Bug Fixes

* **workflow:** disable MR pipeline from prod & integ branches ([3fc4c9e](https://gitlab.com/to-be-continuous/maven/commit/3fc4c9edbded967df2f4c648672de8d51515bd7e))

## [3.9.1](https://gitlab.com/to-be-continuous/maven/compare/3.9.0...3.9.1) (2024-1-30)


### Bug Fixes

* sanitize variable substitution pattern ([f3164e8](https://gitlab.com/to-be-continuous/maven/commit/f3164e86c50e730af74c032ee0fb3c05c7005106))

# [3.9.0](https://gitlab.com/to-be-continuous/maven/compare/3.8.0...3.9.0) (2024-1-27)


### Features

* GitLab CI/CD component migration ([5c32520](https://gitlab.com/to-be-continuous/maven/commit/5c32520f6eecc18b58b2b2cf0f4326e04e023cec))

# [3.8.0](https://gitlab.com/to-be-continuous/maven/compare/3.7.1...3.8.0) (2023-12-8)


### Features

* use centralized tracking image (gitlab.com) ([6d11997](https://gitlab.com/to-be-continuous/maven/commit/6d11997d1894711795685416b3c2aa574b3a77cb))

## [3.7.1](https://gitlab.com/to-be-continuous/maven/compare/3.7.0...3.7.1) (2023-11-02)


### Bug Fixes

* initialize docker auth config in mvn-sbom job for private registries ([4c991ef](https://gitlab.com/to-be-continuous/maven/commit/4c991ef2620fbac31cb4ea6de632c1c4bdb7957e))

# [3.7.0](https://gitlab.com/to-be-continuous/maven/compare/3.6.2...3.7.0) (2023-10-24)


### Features

* inject branch slug into SNAPSHOT version ([6fc6817](https://gitlab.com/to-be-continuous/maven/commit/6fc68178b57c53b77a212901a2735bb0ba04cf54))

## [3.6.2](https://gitlab.com/to-be-continuous/maven/compare/3.6.1...3.6.2) (2023-10-16)


### Bug Fixes

* declare all TBC stages ([00b01f1](https://gitlab.com/to-be-continuous/maven/commit/00b01f12e629ef924dd4eca403540bfa7b1b3765))

## [3.6.1](https://gitlab.com/to-be-continuous/maven/compare/3.6.0...3.6.1) (2023-09-19)


### Bug Fixes

* **release:** fix and clarify Git config in release process ([58320af](https://gitlab.com/to-be-continuous/maven/commit/58320afad0b80d1da398240a19774922daac2bf2))

# [3.6.0](https://gitlab.com/to-be-continuous/maven/compare/3.5.0...3.6.0) (2023-07-02)


### Features

* **jib:** add Maven Jib variant to build container images for your Java applications ([96c2920](https://gitlab.com/to-be-continuous/maven/commit/96c2920b8da419cedefe67e9cd497df146f94b49))

# [3.5.0](https://gitlab.com/to-be-continuous/maven/compare/3.4.0...3.5.0) (2023-05-28)


### Features

* **release:** allow specifying explicit release version ([b158a3b](https://gitlab.com/to-be-continuous/maven/commit/b158a3bcff10d12a841837c3268a8a992cb1095b))
* **release:** implement 2 steps release ([20e8c04](https://gitlab.com/to-be-continuous/maven/commit/20e8c048c1ed05f5abdc6e6c1b8419a050e3864e))
* **release:** support configure release commit comments ([0e59346](https://gitlab.com/to-be-continuous/maven/commit/0e59346132095cb744741e5327c5117c2cda3c5b))

# [3.4.0](https://gitlab.com/to-be-continuous/maven/compare/3.3.1...3.4.0) (2023-05-27)


### Features

* **workflow:** extend (skip ci) feature ([4354aff](https://gitlab.com/to-be-continuous/maven/commit/4354affef66bdf8913413a2761acdc3a281c2bb3))

## [3.3.1](https://gitlab.com/to-be-continuous/maven/compare/3.3.0...3.3.1) (2023-03-28)


### Bug Fixes

* **sbom:** add CycloneDX report ([9773ebe](https://gitlab.com/to-be-continuous/maven/commit/9773ebee8e79161e2d6aafcac56c67997ce4a918))

# [3.3.0](https://gitlab.com/to-be-continuous/maven/compare/3.2.3...3.3.0) (2023-03-22)


### Features

* support settings.xml to be passed as file-type variable ([7775c35](https://gitlab.com/to-be-continuous/maven/commit/7775c35814d687dfb00be60d813ffe5d189347f8))

## [3.2.3](https://gitlab.com/to-be-continuous/maven/compare/3.2.2...3.2.3) (2023-01-27)


### Bug Fixes

* "Add registry name in all Docker images" ([2ef742c](https://gitlab.com/to-be-continuous/maven/commit/2ef742c44b66964a01bf466af61e39809fc91d9a))

## [3.2.2](https://gitlab.com/to-be-continuous/maven/compare/3.2.1...3.2.2) (2022-12-11)


### Bug Fixes

* no-snapshot-deps jobs has no upstream dependencies ([091c4ab](https://gitlab.com/to-be-continuous/maven/commit/091c4ab9d0d73ea9386cae7b5298507f496ba4a4))

## [3.2.1](https://gitlab.com/to-be-continuous/maven/compare/3.2.0...3.2.1) (2022-12-01)


### Bug Fixes

* typo in sbom outputName ([9029fa4](https://gitlab.com/to-be-continuous/maven/commit/9029fa461733ebbe1b138265b74cbb3f72739cee))

# [3.2.0](https://gitlab.com/to-be-continuous/maven/compare/3.1.4...3.2.0) (2022-11-28)


### Features

* add a job generating software bill of materials ([ec6f987](https://gitlab.com/to-be-continuous/maven/commit/ec6f987402b08f88c831a345be183a56fbaa1f20))

## [3.1.4](https://gitlab.com/to-be-continuous/maven/compare/3.1.3...3.1.4) (2022-10-20)


### Bug Fixes

* add MAVEN_DEPENDENCY_CHECK_DISABLED variable ([b26c67c](https://gitlab.com/to-be-continuous/maven/commit/b26c67c4e7210c73b217d87e23772c610316ee0d))
* kicker.json and README for dependency-check and forbid-snapshot-dependencies jobs ([912e0f3](https://gitlab.com/to-be-continuous/maven/commit/912e0f39d0be69fd9ec6d9111b8a0e682e20cdca))

## [3.1.3](https://gitlab.com/to-be-continuous/maven/compare/3.1.2...3.1.3) (2022-10-06)


### Bug Fixes

* **maven:** use Maven CLI options ([2be56aa](https://gitlab.com/to-be-continuous/maven/commit/2be56aa72f08a0f6a2cf483cc9b96cbf23104fd4))

## [3.1.2](https://gitlab.com/to-be-continuous/maven/compare/3.1.1...3.1.2) (2022-10-04)


### Bug Fixes

* remove quotes embeded with value ([d115fd4](https://gitlab.com/to-be-continuous/maven/commit/d115fd46df00dbbcc5ad4dc4cb8b1ac52ede3b9b))

## [3.1.1](https://gitlab.com/to-be-continuous/maven/compare/3.1.0...3.1.1) (2022-09-30)


### Bug Fixes

* add processing to add -X when TRACE is set ([754d309](https://gitlab.com/to-be-continuous/maven/commit/754d309f0146216bed8863aa7a06679ddf36481b))

# [3.1.0](https://gitlab.com/to-be-continuous/maven/compare/3.0.0...3.1.0) (2022-08-10)


### Bug Fixes

* **cache:** fix cache path ([831704e](https://gitlab.com/to-be-continuous/maven/commit/831704e75358e4ce923ae1130a04deb0d99c33bf))


### Features

* manage Sonar task cache in GitLab ([ba82d4c](https://gitlab.com/to-be-continuous/maven/commit/ba82d4cf4e9ef733311e2adc6bb9d24b6d7634eb))
* migrate $SONAR_AUTH_TOKEN to $SONAR_TOKEN (standard) ([841cedf](https://gitlab.com/to-be-continuous/maven/commit/841cedf8b693565ff9f02c650828de2b5d0e71f5))
* migrate $SONAR_URL to $SONAR_HOST_URL (standard) ([0edf601](https://gitlab.com/to-be-continuous/maven/commit/0edf6016dbcbe9e5b63d108736a0a75e02b8fbec))
* remove explicit MR analysis ([3db0b12](https://gitlab.com/to-be-continuous/maven/commit/3db0b125927ea8272b95b7e7533799f428aef520))
* remove support of Sonar GitLab plugin (discontinued) ([167cddd](https://gitlab.com/to-be-continuous/maven/commit/167cddd3b232b49c1f6e932c8bd2dba1a3f41bd9))
* standardize wait for quality gate impl ([d47e40d](https://gitlab.com/to-be-continuous/maven/commit/d47e40df018d30270912c57bfa69eb793b30b49b))

# [3.0.0](https://gitlab.com/to-be-continuous/maven/compare/2.3.0...3.0.0) (2022-08-05)


### Features

* adaptive pipeline ([08a1b5e](https://gitlab.com/to-be-continuous/maven/commit/08a1b5e56fab796f31eeb7f3a0ee28af98a765a3))


### BREAKING CHANGES

* change default workflow from Branch pipeline to MR pipeline

# [2.3.0](https://gitlab.com/to-be-continuous/maven/compare/2.2.0...2.3.0) (2022-05-01)


### Features

* configurable tracking image ([124762b](https://gitlab.com/to-be-continuous/maven/commit/124762bc16b31d7309b38faab58286745340c72b))

# [2.2.0](https://gitlab.com/to-be-continuous/maven/compare/2.1.6...2.2.0) (2022-04-28)


### Features

* Add a MAVEN_PROJECT_DIR ([7bdc6fe](https://gitlab.com/to-be-continuous/maven/commit/7bdc6feed564a6bf912b3a749f04bf2dd0c58a04))

## [2.1.6](https://gitlab.com/to-be-continuous/maven/compare/2.1.5...2.1.6) (2022-04-26)


### Bug Fixes

* migrate deprecated CI_BUILD_REF_NAME variable ([ed46369](https://gitlab.com/to-be-continuous/maven/commit/ed46369a84f43a320356ce44b0c7a3ebd595712e))

## [2.1.5](https://gitlab.com/to-be-continuous/maven/compare/2.1.4...2.1.5) (2022-04-02)


### Bug Fixes

* **dependency-check:** Use aggregate goal to support multi-modules projects ([bbddc72](https://gitlab.com/to-be-continuous/maven/commit/bbddc7248872315711cce4787b06ac2b5c00debd))

## [2.1.4](https://gitlab.com/to-be-continuous/maven/compare/2.1.3...2.1.4) (2022-02-25)


### Bug Fixes

* **artifacts:** always publish test artifacts ([3bcb0bc](https://gitlab.com/to-be-continuous/maven/commit/3bcb0bc547911bc08bd56f462d74159c0d4831da))

## [2.1.3](https://gitlab.com/to-be-continuous/maven/compare/2.1.2...2.1.3) (2022-02-04)


### Bug Fixes

* Use Dmaven.test.skip to avoid compiling and running tests instead of DskipTests ([d7c2da1](https://gitlab.com/to-be-continuous/maven/commit/d7c2da14743a385dd13783a953b8a140ab0bca27))

## [2.1.2](https://gitlab.com/to-be-continuous/maven/compare/2.1.1...2.1.2) (2021-10-07)


### Bug Fixes

* use master or main for production env ([d5cac44](https://gitlab.com/to-be-continuous/maven/commit/d5cac44ae499b9ab3063cdb31935a2cd9d1b448a))

## [2.1.1](https://gitlab.com/to-be-continuous/maven/compare/2.1.0...2.1.1) (2021-09-23)


### Bug Fixes

* mvn-release missing reusing .mvn-base before_script ([2d87f8d](https://gitlab.com/to-be-continuous/maven/commit/2d87f8d0563eee8b6fcfa147938337180e32fa70))

# [2.1.0](https://gitlab.com/to-be-continuous/maven/compare/2.0.1...2.1.0) (2021-09-13)


### Features

* auto-detect Maven settings file ([70f04e3](https://gitlab.com/to-be-continuous/maven/commit/70f04e3c4e9fb50b471fd1d832ffcfec1d76f411))

## [2.0.1](https://gitlab.com/to-be-continuous/maven/compare/2.0.0...2.0.1) (2021-09-07)

### Bug Fixes

* maven-enforcer-plugin version upgrade ([30dcc01](https://gitlab.com/to-be-continuous/maven/commit/30dcc012c26fcdaf38ac3596906717f095a6c6bd))

## [2.0.0](https://gitlab.com/to-be-continuous/maven/compare/1.4.2...2.0.0) (2021-09-03)

### Features

* Change boolean variable behaviour ([16ead86](https://gitlab.com/to-be-continuous/maven/commit/16ead8655048161dd52e6a699dd6a0f023e7d0d7))

### BREAKING CHANGES

* boolean variable now triggered on explicit 'true' value

Signed-off-by: Cédric OLIVIER <cedric3.olivier@orange.com>

## [1.4.2](https://gitlab.com/to-be-continuous/maven/compare/1.4.1...1.4.2) (2021-06-15)

### Bug Fixes

* **sonar:** prevent shallow git clone (required by Sonar Scanner) ([4dbd90e](https://gitlab.com/to-be-continuous/maven/commit/4dbd90e47805b09317702ba643929f88322b94df))

## [1.4.1](https://gitlab.com/to-be-continuous/maven/compare/1.4.0...1.4.1) (2021-06-15)

### Bug Fixes

* autodetect MR when a milestone is here ([c4fbdf3](https://gitlab.com/to-be-continuous/maven/commit/c4fbdf37d3e07f7980ee152b37f0e8978a2d129e))

## [1.4.0](https://gitlab.com/to-be-continuous/maven/compare/1.3.0...1.4.0) (2021-06-10)

### Features

* move group ([df3a46f](https://gitlab.com/to-be-continuous/maven/commit/df3a46f19e33da869ffcea9e7b879029ad915a21))

## [1.3.0](https://gitlab.com/Orange-OpenSource/tbc/maven/compare/1.2.0...1.3.0) (2021-06-07)

### Bug Fixes

* use curl instead of wget in get_latest_template_version script ([96b191f](https://gitlab.com/Orange-OpenSource/tbc/maven/commit/96b191f8211e7957858ad58d2997f0a71391c534))

### Features

* **sonar:** autodetect Merge Request from current branch ([10c3058](https://gitlab.com/Orange-OpenSource/tbc/maven/commit/10c3058fd379e1b989ac81b3caba84fbc347552c))

## [1.2.0](https://gitlab.com/Orange-OpenSource/tbc/maven/compare/1.1.2...1.2.0) (2021-05-18)

### Features

* add scoped variables support ([9089860](https://gitlab.com/Orange-OpenSource/tbc/maven/commit/9089860cba63991fec586ddfe44304fe3e4df4c9))

## [1.1.2](https://gitlab.com/Orange-OpenSource/tbc/maven/compare/1.1.1...1.1.2) (2021-05-12)

### Bug Fixes

* make semrel integration disableable ([dd29f28](https://gitlab.com/Orange-OpenSource/tbc/maven/commit/dd29f287da033a6945b4f75aa768c380120438ae))

## [1.1.1](https://gitlab.com/Orange-OpenSource/tbc/maven/compare/1.1.0...1.1.1) (2021-05-12)

### Bug Fixes

* **forbid-snapshot-dependencies:** use CLI options ([24cfb7b](https://gitlab.com/Orange-OpenSource/tbc/maven/commit/24cfb7bdc5ef66717bb75de99784049744bd092b))

## [1.1.0](https://gitlab.com/Orange-OpenSource/tbc/maven/compare/1.0.0...1.1.0) (2021-05-07)

### Features

* add forbid snapshot dependencies job ([295f385](https://gitlab.com/Orange-OpenSource/tbc/maven/commit/295f38530193f62876f6167fa5fd118c4fa5119c))
* add semantic-release integration ([d99c6bb](https://gitlab.com/Orange-OpenSource/tbc/maven/commit/d99c6bbf811d37e7e7152063f5f1fc5de230c37a))

## 1.0.0 (2021-05-06)

### Features

* initial release ([67ee980](https://gitlab.com/Orange-OpenSource/tbc/maven/commit/67ee980ac5acf69b9bf9cf3c71d7a2d9c1385bd1))
