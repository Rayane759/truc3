# GitLab CI template for Maven

This project implements a GitLab CI/CD template to build, test and analyse your [Maven](https://maven.apache.org/)-based projects.

## Usage

This template can be used both as a [CI/CD component](https://docs.gitlab.com/ci/components/#use-a-component) 
or using the legacy [`include:project`](https://docs.gitlab.com/ci/yaml/#includeproject) syntax.

### Use as a CI/CD component

Add the following to your `.gitlab-ci.yml`:

```yaml
include:
  # 1: include the component
  - component: $CI_SERVER_FQDN/to-be-continuous/maven/gitlab-ci-maven@5.4.0
    # 2: set/override component inputs
    inputs:
      # ⚠ this is only an example
      image: docker.io/library/maven:3.8-openjdk-18
      deploy-enabled: true
```

### Use as a CI/CD template (legacy)

Add the following to your `.gitlab-ci.yml`:

```yaml
include:
  # 1: include the template
  - project: 'to-be-continuous/maven'
    ref: '5.4.0'
    file: '/templates/gitlab-ci-maven.yml'

variables:
  # 2: set/override template variables
  # ⚠ this is only an example
  MAVEN_IMAGE: docker.io/library/maven:3.8-openjdk-18
  MAVEN_DEPLOY_ENABLED: "true"
```

## Global configuration

The Maven template uses some global configuration throughout all jobs.

| Input / Variable                    | Description                                                                                                        | Default value |
| --------------------- |--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `image` / `MAVEN_IMAGE`             | The Docker image used to run Maven <br/>:warning: **set the version required by your project**                     | `docker.io/library/maven:latest` <br/>[![Trivy Badge](https://to-be-continuous.gitlab.io/doc/secu/trivy-badge-MAVEN_IMAGE.svg)](https://to-be-continuous.gitlab.io/doc/secu/trivy-MAVEN_IMAGE) |
| `project-dir` / `MAVEN_PROJECT_DIR` | Maven projet root directory                                                                                        | `.` |
| `cfg-dir` / `MAVEN_CFG_DIR`         | The Maven configuration directory                                                                                  | `.m2` |
| `settings-file` / `MAVEN_SETTINGS_FILE` | The Maven `settings.xml` file path                                                                             | `${MAVEN_CFG_DIR}/settings.xml` |
| `opts` / `MAVEN_OPTS`               | [Global Maven options](http://maven.apache.org/configure.html#maven_opts-environment-variable)                     | `-Dhttps.protocols=TLSv1.2 -Dmaven.repo.local=${MAVEN_CFG_DIR}/repository -Dorg.slf4j.simpleLogger.showDateTime=true -Djava.awt.headless=true` |
| `cli-opts` / `MAVEN_CLI_OPTS`       | Additional [Maven options](https://maven.apache.org/ref/3-LATEST/maven-embedder/cli.html) used on the command line | `--no-transfer-progress --batch-mode --errors --fail-at-end --show-version -DinstallAtEnd=true -DdeployAtEnd=true` |

### About `$MAVEN_IMAGE`

Each job in the template will use the defined container image to provide the Maven and Java runtime to the job context.
That's why it is mandatory that you set the version of Maven as required by your project (e.g. `docker.io/library/maven:3.9.9-eclipse-temurin-21` for Maven 3.9.9 on Eclipse Temurin JDK 21).

#### Use of the Maven Wrapper

Maven Wrapper - although very convenient for the developer to automatically download and use the required Maven version on each developer environment - is **not supported by this template**.
We consider reinstalling over and over again another version of Maven in every job would be dumb: better pull directly an image with the right version.
			
### About `$MAVEN_CFG_DIR`

This variable is used to define the Maven configuration directory. It is used to declare the cache policy and marked the `${MAVEN_CFG_DIR}/repository` directory as cached (not to download Maven dependencies over and over again).

If you have a good reason to do differently, you'll have to override the `MAVEN_CLI_OPTS` variable as well as the [`cache`](https://docs.gitlab.com/ci/yaml/#cache) policy.

### About `$MAVEN_SETTINGS_FILE`

If a file is found at the `$MAVEN_SETTINGS_FILE` location, the template automatically uses it as a `settings.xml` (using the [`--settings` option](https://maven.apache.org/ref/current/maven-embedder/cli.html) on command line).

Note that with this design you are free to either:

1. inline the `settings.xml` file into your repository source (:warning: make sure not to inline secrets but use the `${env.MY_PASSWORD}` replacement pattern instead and define the `MY_PASSWORD` variable as secret project variable),
2. or define the `settings.xml` content as a [file type project variable](https://docs.gitlab.com/ci/variables/#use-file-type-cicd-variables).

## Jobs

### `mvn-build` job

The Maven template features a job `mvn-build` that performs **build and tests** at once.
This stage is performed in a single job for **optimization** purpose (it saves time) and also
for test jobs dependency reasons (some test jobs such as SONAR analysis have a dependency on test results).

It uses the following variable:

| Input / Variable      | Description                              | Default value     |
| --------------------- | ---------------------------------------- | ----------------- |
| `build-args` / `MAVEN_BUILD_ARGS` | Maven arguments for the build & test job | `org.jacoco:jacoco-maven-plugin:prepare-agent verify org.jacoco:jacoco-maven-plugin:report` |

#### About Code Coverage

With its default arguments, the GitLab CI template for Maven forces the use of [JaCoCo Maven Plugin](https://www.eclemma.org/jacoco/trunk/doc/maven.html)
to compute code coverage during unit tests execution.

In addition it makes the necessary to [integrate code coverage stats into your GitLab project](https://docs.gitlab.com/ci/testing/code_coverage/#view-coverage-results) (report badge and viewable coverage in merge requests).

If you want to fix the JaCoCo plugin version or tweak the default configuration, you may have to configure the
[JaCoCo Maven Plugin](https://www.eclemma.org/jacoco/trunk/doc/maven.html) in your `pom.xml`, but be aware of the
following:

* do not declare JaCoCo executions for `prepare-agent` and `report` goals as each would run twice during
  unit tests (not necessarily with the expected configuration). If you really need to do so anyway, you'll have to
  override the `$MAVEN_BUILD_ARGS` variable to remove the explicit invocation to JaCoCo goals.
* make sure the `report` goal computes a CSV report (that's default behavior), that is used by the Maven template to compute the global coverage stat,
* make sure the `report` goal computes an XML report (that's default behavior), that is required to support [GitLab code coverage intergation](https://docs.gitlab.com/ci/testing/code_coverage/jacoco/).

More info:

* [Maven Surefire Plugin](https://maven.apache.org/surefire/maven-surefire-plugin)
* [`surefire:test` parameters](https://maven.apache.org/surefire/maven-surefire-plugin/usage.html)

### `mvn-sonar` job — SonarQube analysis

This job, **disabled by default**, is bound to the `test` stage and performs a SonarQube analysis of your code.
This job uses the following variables:

| Input / Variable         | Description                            | Default value     |
| ------------------------ | -------------------------------------- | ----------------- |
| `sonar-host-url` / `SONAR_HOST_URL` | SonarQube server url                   | _none_ (disabled) |
| :lock: `SONAR_TOKEN`     | SonarQube authentication [token](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-tokens/#using-a-token) (depends on your authentication method) | _none_ |
| :lock: `SONAR_LOGIN`     | SonarQube [login](https://docs.sonarsource.com/sonarqube-server/extension-guide/web-api/#http-basic-access) (depends on your authentication method)                | _none_ |
| :lock: `SONAR_PASSWORD`  | SonarQube password (depends on your authentication method)             | _none_ |
| `sonar-base-args` / `SONAR_BASE_ARGS` | SonarQube [analysis arguments](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters/) | `org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.links.homepage=${CI_PROJECT_URL} -Dsonar.links.ci=${CI_PROJECT_URL}/-/pipelines -Dsonar.links.issue=${CI_PROJECT_URL}/-/issues` |
| `sonar-quality-gate-enabled` / `SONAR_QUALITY_GATE_ENABLED` | Set to `true` to enable SonarQube [Quality Gate](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction/) verification.<br/>_Uses `sonar.qualitygate.wait` parameter ([see doc](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/overview/#quality-gate-fails))._ | _none_ (disabled) |

#### Recommended minimal configuration

1. set the `SONAR_HOST_URL` value either in your `.gitlab-ci.yml` file or as a project or group variable (:warning: setting it as a group variable will enable the SonarQube analysis for all the children projects),
2. define your SonarQube credentials (:lock: `SONAR_TOKEN` or `SONAR_LOGIN` & :lock: `SONAR_PASSWORD`) as project or group variables,
3. configure the project SonarQube settings in the `pom.xml` file (:warning: the [SonarScanner for Maven](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-maven/#configuring-analysis) completely ignores the `sonar-project.properties` file):
    ```xml
    <properties>
      <!-- the SonarQube project key -->
      <sonar.projectKey>write-key-here</sonar.projectKey>
      <!-- additional SonarQube settings can go here -->
      ...
    </properties>
    ```
    More info about [SonarQube settings](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-maven/#analyzing)

:warning: if using [SonarCloud](https://docs.sonarsource.com/sonarqube-cloud/) (a cloud-based SonarQube-as-a-Service), you'll have to define the additional `sonar.organization` property ([see mandatory-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters/#mandatory-parameters)).

:information_source: As SonarCloud determined the `organization` and `projectKey` properties from the project's GitLab context when importing the project, you can reuse the predefined GitLab variables as follows in your `pom.xml`:
```xml
<properties>
  <!-- SonarCloud settings -->
  <sonar.organization>${env.CI_PROJECT_ROOT_NAMESPACE}</sonar.organization>
  <sonar.projectKey>${env.CI_PROJECT_ROOT_NAMESPACE}_${env.CI_PROJECT_NAME}</sonar.projectKey>
</properties>
```

#### Automatic Branch Analysis & Merge Request Analysis

This template relies on SonarScanner's [GitLab integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/introduction/), which is able to auto-detect whether to launch Branch Analysis or Merge Request Analysis
from GitLab's environment variables.

:warning: This feature also depends on your SonarQube server version and license.
If using Community Edition, you'll have to install the [sonarqube-community-branch-plugin](https://github.com/mc1arke/sonarqube-community-branch-plugin) to enable automatic Branch & Merge Request analysis (only works from SonarQube version 8).

:warning: Merge Request Analysis only works if you're running [Merge Request pipeline](https://docs.gitlab.com/ci/yaml/workflow/#switch-between-branch-pipelines-and-merge-request-pipelines) strategy (default).

#### Disable the job

> :information_source: See [Usage](https://to-be-continuous.gitlab.io/doc/usage/#example-3-disable-go-mod-outdated-job) 
> for more information about disabling any job that MAY not be required in a project or group.

Without disabling the job, you can still exclude a particular project by defining a property `<sonar.skip>true</sonar.skip>` in the pom.xml of the project or module you want to exclude.

**Output artifacts:**

When the SonarQube [Quality Gate](https://docs.sonarsource.com/sonarqube-server/latest/quality-standards-administration/managing-quality-gates/introduction/) is enabled (using `sonar-quality-gate-enabled` / `SONAR_QUALITY_GATE_ENABLED`), this job produces a GitLab SAST report `mvn-sonar.gitlab-sast.json`, generated from SonarQube as part of the [Vulnerability Reporting integration](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/gitlab-integration/setting-up-at-project-level#reporting-vulnerabilities), containing the detected security findings. Artifacts are retained for one day and are downloadable only by users with the Developer role or higher in GitLab.

The following reports are generated:

| Report         | Format                                                                       | Usage             |
| -------------- | ---------------------------------------------------------------------------- | ----------------- |
| `$MAVEN_PROJECT_DIR/reports/mvn-sonar.gitlab-sast.json` | [Gitlab SAST](https://gitlab.com/gitlab-org/security-products/security-report-schemas/-/blob/master/src/sast-report-format.json?ref_type=heads) report | [GitLab integration](https://docs.gitlab.com/ci/yaml/artifacts_reports/#artifactsreportssast) |

### `mvn-dependency-check` job

This job enables a manual [Dependency-Check](https://jeremylong.github.io/DependencyCheck/dependency-check-maven/configuration.html)
analysis.

It is bound to the `test` stage, and uses the following variables:

| Input / Variable      | Description                            | Default value     |
| --------------------- | -------------------------------------- | ----------------- |
| `dependency-check-disabled` / `MAVEN_DEPENDENCY_CHECK_DISABLED` | Set to `true` to disable this job | _none_ |
| `dependency-check-args` / `MAVEN_DEPENDENCY_CHECK_ARGS` | Maven arguments for Dependency Check job | `org.owasp:dependency-check-maven:check -DretireJsAnalyzerEnabled=false -DassemblyAnalyzerEnabled=false` |


A Dependency Check is a quite long operation and therefore the job is configured to be ran __manually__ by default.

However, if you want to enable an automatic Dependency-Check scan, you will have to override the `rules` keyword for the `mvn-dependency-check` job.

Dependency-Check fetches its vulnerbility database from the NVD API which has rate limiting. Using an NVD API key, the rate limit is higher which reduces the execution time of Dependency-Check.

In order to configure an NVD API key you need to:

* Set the `NVD_API_KEY` variable with your NVD API key. :warning: This is a sensitive value, so we recommend you add it as a **masked** Gitlab variable
* Add `-DnvdApiKey=$NVD_API_KEY` to `MAVEN_DEPENDENCY_CHECK_ARGS`

In case your Gitlab runners cannot contact the NVD API (e.g. if they are not allowed to connect to the Internet), you can maintain a local data feed cache with the [vulnz](https://github.com/jeremylong/open-vulnerability-cli) tool.

In order to configure Dependency-Check to fetch the vulnerabilities from your cache you need to:

* Run the [vulnz](https://github.com/jeremylong/open-vulnerability-cli) tool in order to fetch the vulnerabilities and store them as data feeds (the data feeds will be stored as JSON files with the NVD Vulnerability Data API version 2.0 schema)
* Make these data feeds accessible via a URL reachable by your Gitlab runners
* Add `-DnvdDatafeedUrl=https://URL-OF-LOCAL-CACHE` to `MAVEN_DEPENDENCY_CHECK_ARGS`

Furthermore, if you want to upload Dependency-Check reports to SonarQube, you have to:

* Move `mvn-dependency-check` to the `build` stage
* Add `-Dformats=html,json,xml` to `MAVEN_DEPENDENCY_CHECK_ARGS` to output reports
    * HTML report to read the report on SonarQube UI
    * JSON report to create SonarQube issues from the report
    * XML report to import into DefectDojo security dashboard
* Add `-Dsonar.dependencyCheck.htmlReportPath` and `-Dsonar.dependencyCheck.jsonReportPath` with the paths of the generated html and json reports to SonarQube arguments.

More info:

* [Maven Dependency-Check Plugin](https://jeremylong.github.io/DependencyCheck/dependency-check-maven/configuration.html)

### `mvn-no-snapshot-deps` job

This job checks if the project has release-only dependencies, i.e., no `_*-SNAPSHOT_` versions, using the [Maven Enforcer](https://maven.apache.org/enforcer/enforcer-rules/requireReleaseDeps.html) plugin.

Failure is allowed in feature branches.

It is bound to the `test` stage, and uses the following variables:

| Input / Variable      | Description                            | Default value     |
| --------------------- | -------------------------------------- | ----------------- |
| `mvn-forbid-snapshot-dependencies-disabled` / `MVN_FORBID_SNAPSHOT_DEPENDENCIES_DISABLED` | Set to `true` to disable this job | _none_ |

### `mvn-sbom` job

This job generates a [SBOM](https://cyclonedx.org/) file listing all dependencies using [cyclonedx-maven-plugin](https://github.com/CycloneDX/cyclonedx-maven-plugin).

It is bound to the `test` stage, and uses the following variables:

| Input / Variable | Description                            | Default value     |
| --------------------- | -------------------------------------- | ----------------- |
| `sbom-disabled` / `MAVEN_SBOM_DISABLED` | Set to `true` to disable this job | _none_ |
| `TBC_SBOM_MODE`                      | Controls when SBOM reports are generated (`onrelease`: only on `$INTEG_REF`, `$PROD_REF` and `$RELEASE_REF` pipelines; `always`: any pipeline).<br/>:warning: `sbom-disabled` / `DOCKER_SBOM_DISABLED` takes precedence | `onrelease` |
| `sbom-gen-args` / `MAVEN_SBOM_GEN_ARGS` | Maven command used for SBOM analysis | `org.cyclonedx:cyclonedx-maven-plugin:makeAggregateBom` |

### `mvn-release` &amp; `mvn-deploy-*` jobs

These jobs are **disabled by default** and - when enabled - respectively perform the following:

1. a [Maven release:prepare](https://maven.apache.org/maven-release/maven-release-plugin/usage/prepare-release.html) of your current branch
    * only triggers the first part of the release (version changes in `pom.xml`, Git commits and version tag)
    * provides a default integration with `semantic-release` ([see below](#semantic-release-integration))
    * the second part of the release (package and publish to a Maven registry) is performed by the `mvn-deploy` job below
2. a [Maven deploy](https://maven.apache.org/plugins/maven-deploy-plugin/) of your Java packages (jar, war, etc.) to any Maven-compliant registry
    * `mvn-deploy-release` publishes the **stable** version on the tag pipeline triggered by a `mvn-release`,
    * `mvn-deploy-snapshot` publishes the **snapshot** version on other branches.

They are bound to the `publish` stage, and use the following variables:

| Input / Variable                    | Description                                                  | Default value     |
| ----------------------------------- | ------------------------------------------------------------ | ----------------- |
| `deploy-enabled` / `MAVEN_DEPLOY_ENABLED` | Set to `true` to enable release and publish jobs             | _none_ (disabled) |
| `deploy-from-unprotected-disabled` / `MAVEN_DEPLOY_FROM_UNPROTECTED_DISABLED` | Set to `true` to limit snapshot publication to protected branches | _none_ (disabled) |
| `deploy-snapshot-with-slug-enabled` / `MAVEN_DEPLOY_SNAPSHOT_WITH_SLUG_ENABLED` | Set to `true` to inject the Git branch slug in SNAPSHOT versions | _none_ (disabled) |
| `deploy-args` / `MAVEN_DEPLOY_ARGS` | Maven arguments for the `mvn-deploy` job                     | `deploy -Dmaven.test.skip=true` |
| `release-args` / `MAVEN_RELEASE_ARGS` | Maven arguments for the `mvn-release` job                    | `release:prepare -DtagNameFormat=@{project.version} -Darguments=-Dmaven.test.skip=true` |
| `release-version` / `MAVEN_RELEASE_VERSION` | Explicit version to use when triggering a release | _none_ (uses the current snapshot version from `pom.xml`) |
| `release-scm-comment-prefix` / `MAVEN_RELEASE_SCM_COMMENT_PREFIX` | Maven release plugin [scmCommentPrefix](https://maven.apache.org/maven-release/maven-release-plugin/prepare-mojo.html#scmCommentPrefix) parameter | `chore(maven-release): ` |
| `release-scm-release-comment` / `MAVEN_RELEASE_SCM_RELEASE_COMMENT` | Maven release plugin [scmReleaseCommitComment](https://maven.apache.org/maven-release/maven-release-plugin/prepare-mojo.html#scmReleaseCommitComment) parameter (since Maven `3.0.0-M1`) | _none_ (Maven default) |
| `release-scm-dev-comment` / `MAVEN_RELEASE_SCM_DEV_COMMENT` | Maven release plugin [scmDevelopmentCommitComment](https://maven.apache.org/maven-release/maven-release-plugin/prepare-mojo.html#scmDevelopmentCommitComment) parameter (since Maven `3.0.0-M1`) | _none_ (Maven default) |
| `mvn-semrel-release-disabled` / `MVN_SEMREL_RELEASE_DISABLED` | Set to `true` to disable [semantic-release integration](#semantic-release-integration)   | _none_ (disabled) |
| `GIT_USER_NAME` | Git user name to use when committing (global TBC variable) | `$GITLAB_USER_NAME` |
| `GIT_USER_EMAIL` | Git user email to use when committing (global TBC variable) | `$GITLAB_USER_EMAIL` |
| :lock: `GIT_SIGNING_KEY_GPG` | Git GPG signing key to use for commit signing (global TBC variable) | _none_ (disabled) |
| :lock: `GIT_SIGNING_KEY_SSH` | Git SSH signing key to use for commit signing (global TBC variable) | _none_ (disabled) |

More info:

* [Maven Deploy Plugin](https://maven.apache.org/plugins/maven-deploy-plugin/)
* [Maven Release Plugin](http://maven.apache.org/maven-release/maven-release-plugin/index.html)

#### Inject the Git branch slug in SNAPSHOT versions

In order to **segregate your SNAPSHOT versions per branch**, the Maven template allows you to add the Git branch slug into the pom version.
Thus, any other project willing to use your SNAPSHOT packages will be able to do so, explicitly setting its dependency on the desired version (branch).
Only the production branch (`main` or `master` by default) will be preserved from this behavior.

This feature can be enabled setting `MAVEN_DEPLOY_SNAPSHOT_WITH_SLUG_ENABLED` to `true`.

Example: for a project with `<version>1.2.1-SNAPSHOT</version>` in its `pom.xml`:

| Branch                           | Altered version |
| -------------------------------- | ------------------------------------------------------------ |
| `feature/support-facebook-login` | `1.2.1-feature-support-facebook-login-SNAPSHOT` |
| `fix/timedate-serialization`     | `1.2.1-fix-timedate-serialization-SNAPSHOT` |
| `develop` (integration branch)   | `1.2.1-develop-SNAPSHOT` |
| `main` (production branch)       | `1.2.1-SNAPSHOT` |

#### `semantic-release` integration

If you activate the [`semantic-release-info` job from the `semantic-release` template](https://gitlab.com/to-be-continuous/semantic-release/#semantic-release-info-job), the `mvn-release` job will rely on the generated next version info.

* the release will only be performed if a semantic release is present
* the version is passed to the Maven Release plugin as the release version argument adding `-DreleaseVersion=${SEMREL_INFO_NEXT_VERSION}` to the `MAVEN_RELEASE_ARGS` value

:warning: Both the Maven Release plugin and semantic-release template use a dedicated tag format that need to be set accordingly.
By default, the Maven Release plugin uses `${artifactId}-${version}` and semantic-release uses `${version}`
For exemple you can modify the semantic-release tag format with the `SEMREL_TAG_FORMAT` variable (see [semantic-release template variables](https://gitlab.com/to-be-continuous/semantic-release/#variables)).

:information_source: semantic-release determines the next release version from the existing tags in the Git repository. As the default semantic-release tag format (`${version}`) is _not_ the Maven default, if leaving defaults, semantic-release will always determine the next version to release as `1.0.0`, trying to keep overwriting the same version.
In addition to the functional problem, this might result in a release failure as soon as trying to release version `1.0.0` for the second time (as Maven repos configured as "release" repos will not permit overwriting).
Simply set `SEMREL_TAG_FORMAT` as shown below to have the semantic-release tag format match the maven release plugin one.

```yml
variables:
  # double dollar to prevent evaluation (escape char)
  SEMREL_TAG_FORMAT: "myArtifactId-$${version}"
```

Or you can [override the maven release plugin tag format](https://maven.apache.org/maven-release/maven-release-plugin/usage/prepare-release.html#overriding-the-default-tag-name-format).

Note: It is the `mvn-release` job that will perform the release and so you only need the `semantic-release-info` job. Set the `SEMREL_RELEASE_DISABLED` variable as shown below.

```yml
variables:
  SEMREL_RELEASE_DISABLED: "true"
```

Finally, the semantic-release integration can be disabled with the `MVN_SEMREL_RELEASE_DISABLED` variable.

#### Maven repository authentication

Your Maven repository may require authentication credentials to publish artifacts.

You may handle them in the following ways:

1. define all required credentials as :lock: [project variables](https://docs.gitlab.com/ci/variables/#for-a-project),
2. make sure your `pom.xml` (or ancestor) [declares your `<repository>` and `<snapshotRepository>` with server **id**s in a `<distributionManagement>` section](https://maven.apache.org/pom.html#repository),
3. in your `${MAVEN_CFG_DIR}/settings.xml` file, [define the repository servers credentials in the `<servers>` section](https://maven.apache.org/settings.html#Servers) using the `${env.VARIABLE}` pattern—will be automatically evaluated and replaced by Maven.

**Example 1** — using the [GitLab Maven Repository](https://docs.gitlab.com/user/packages/maven_repository/)

`pom.xml`:

```xml
<!-- ... -->
<distributionManagement>
  <snapshotRepository>
      <id>gitlab-maven</id>
      <url>${env.CI_API_V4_URL}/projects/${env.CI_PROJECT_ID}/packages/maven</url>
  </snapshotRepository>
  <repository>
      <id>gitlab-maven</id>
      <url>${env.CI_API_V4_URL}/projects/${env.CI_PROJECT_ID}/packages/maven</url>
  </repository>
</distributionManagement>
<!-- ... -->
```

`${MAVEN_SETTINGS_FILE}`:

```xml
<settings>
  <servers>
    <!-- required when using GitLab's package registry to deploy -->
    <!-- see: https://docs.gitlab.com/user/packages/maven_repository/index/#use-the-gitlab-endpoint-for-maven-packages -->
    <server>
        <id>gitlab-maven</id>
        <configuration>
            <httpHeaders>
                <property>
                    <name>Job-Token</name>
                    <value>${env.CI_JOB_TOKEN}</value>
                </property>
            </httpHeaders>
        </configuration>
    </server>
  </servers>
</settings>
```

**Example 2** — using an Artifactory repository with same credentials for snapshot &amp; release

`pom.xml`:

```xml
<!--... -->
<distributionManagement>
  <snapshotRepository>
    <id>artifactory</id>
    <url>https://artifactory.acme.host/artifactory/maven-snapshot-repo</url>
  </snapshotRepository>
  <repository>
    <id>artifactory</id>
    <url>https://artifactory.acme.host/artifactory/maven-release-repo</url>
  </repository>
</distributionManagement>
<!--...-->
```

`${MAVEN_CFG_DIR}/settings.xml`:

```xml
<settings>
  <servers>
    <server>
      <id>artifactory</id>
      <username>${env.ARTIFACTORY_USER}</username>
      <password>${env.ARTIFACTORY_PASSWORD}</password>
    </server>
  </servers>
  <mirrors>
    <mirror>
      <id>artifactory.mirror</id>
      <mirrorOf>central</mirrorOf>
      <name>Artifactory Maven 2 central repository mirror</name>
      <url>https://artifactory.acme.host/artifactory/maven-virtual-repo/</url>
    </mirror>
  </mirrors>
</settings>
```

#### SCM authentication

A Maven release involves some Git push operations.

You can either use an `ssh` key or an authenticated and authorized Git user.

##### Using an SSH key

We recommend you to use a [project deploy key](https://docs.gitlab.com/user/project/deploy_keys/#project-deploy-keys) with write access to your project.

The key should not have a passphrase (see [how to generate a new SSH key pair](https://docs.gitlab.com/user/ssh/#generate-an-ssh-key-pair)).

Note: It is strongly recommended to use a Service Account user (GitLab Premium feature), rather than a human user, to create the deploy key. This helps avoid the risks and limitations outlined in the [Security implications](https://docs.gitlab.com/user/project/deploy_keys/#security-implications) section.

Specify :lock: `$GIT_PRIVATE_KEY` as protected project variable with the private part of the deploy key.

```PEM
-----BEGIN 0PENSSH PRIVATE KEY-----
blablabla
-----END OPENSSH PRIVATE KEY-----
```

The template handles both classic variable and file variable.

:warning: The `scm` connections in your `pom.xml` should use the `ssh` protocol

```xml
  <scm>
    <connection>scm:git:ssh://git@gitlab-host/path/to/my/project.git</connection>
    <developerConnection>scm:git:ssh://git@gitlab-host/path/to/my/project.git</developerConnection>
    ...
  </scm>
```

##### Using Git user authentication

Simply specify :lock: `$GIT_USER_NAME` and :lock: `$GIT_PASSWORD` as protected project variables, and they will be dynamically 
evaluated and appended to the Maven release arguments.

Note that the password should be an access token with `write_repository` scope and `Maintainer` role.

:warning: The `scm` connections in your `pom.xml` should use the `https` protocol

```xml
  <scm>
    <connection>scm:git:https://gitlab-host/path/to/my/project.git</connection>
    <developerConnection>scm:git:https://gitlab-host/path/to/my/project.git</developerConnection>
    ...
  </scm>
```

#### Working around Push Rules

A Maven release involves some Git commit and push operations, which might fail in projects where one or more [push rules](https://docs.gitlab.com/user/project/repository/push_rules/) have been activated.

##### "Reject unverified users" and "Reject inconsistent user name" push rules

With these rules enabled, the Git push will fail unless the commit author name and committer email match the name and email of the user that _authenticated the push_.
* If an **SSH key** is used, this will be the user associated with that SSH key.
* If a **deploy key** is used, this will be the user that created the deploy key.
* If a **deploy token** is used, this will be the deploy token bot user.

During a Maven release, however, the Git user name and email will be derived from the user that _triggered the release job_ instead, which may or may not be the same user.

To work around this, you can explicitly set the `$GIT_USER_NAME` and `$GIT_USER_EMAIL` variables to the appropriate user's name and email.

##### "Reject unsigned commits" push rule

With this rule enabled, the Git push will fail unless all commits are signed.

While GitLab supports commit signing via GPG, SSH, and X.509, the Maven template currently only supports GPG and SSH.

###### Automatic commit signing using GPG

To enable automatic commit signing using GPG, you must generate a GPG keypair, add its public key to the appropriate user, and configure its private key as the :lock: `$GIT_SIGNING_KEY_GPG` protected project variable.

###### Automatic commit signing using SSH

To enable automatic commit signing using SSH, you must generate an SSH keypair, add its public key to the appropriate user (with usage type `Signing`), and configure its private key as the :lock: `$GIT_SIGNING_KEY_SSH` protected project variable.

:warning: SSH commit signing requires Git version 2.34 or higher in your build image.

Note: If you are already using SSH key authentication using `$GIT_PRIVATE_KEY`, the same SSH key can be used for commit signing, provided its usage type was set to `Authentication & Signing`. You can configure this as follows:

```yaml
variables:
  GIT_SIGNING_KEY_SSH: "${GIT_PRIVATE_KEY}"
```

## Variants

### Jib variant

This variant builds optimized Docker and OCI images for your Java applications (without deep mastery of Docker best-practices) with [Jib](https://github.com/GoogleContainerTools/jib).

#### Configuration

This variant uses the [Jib Maven Plugin](https://github.com/GoogleContainerTools/jib/tree/master/jib-maven-plugin) to build a Docker container and publish that container to a registry.

##### Images and registries config

| Input / Variable | Description              | Default value                                     |
| -------------------------------------------- | ------------------------ | ------------------------------------------------- |
| `jib-snapshot-image` / `MAVEN_JIB_SNAPSHOT_IMAGE` | Container snapshot image | `$CI_REGISTRY_IMAGE/snapshot:$CI_COMMIT_REF_SLUG` |
| `jib-release-image` / `MAVEN_JIB_RELEASE_IMAGE` | Container release image  | `$CI_REGISTRY_IMAGE:$CI_COMMIT_REF_NAME`          |
| :lock: `MAVEN_JIB_REGISTRY_USER`             | Default registry username for image registry | `$CI_REGISTRY_USER` _(default GitLab registry user)_ |
| :lock: `MAVEN_JIB_REGISTRY_PASSWORD`         | Default registry password for image registry  | `$CI_REGISTRY_PASSWORD` _(default GitLab registry password)_ |
| :lock: `MAVEN_JIB_REGISTRY_SNAPSHOT_USER`    | Registry username for snapshot image registry.<br/> Only set if different from default. | _none_ |
| :lock: `MAVEN_JIB_REGISTRY_SNAPSHOT_PASSWORD`| Registry password for snapshot image registry.<br/> Only set if different from default. | _none_ |
| :lock: `MAVEN_JIB_REGISTRY_RELEASE_USER`     | Registry username for release image registry.<br/> Only set if different from default. | _none_ |
| :lock: `MAVEN_JIB_REGISTRY_RELEASE_PASSWORD` | Registry password for release image registry.<br/> Only set if different from default. | _none_ |

The template uses GitLab registries and authentication defaults. See the Docker template for configuring alternate [registries and credentials](https://gitlab.com/to-be-continuous/docker#registries-and-credentials).

##### Security scanning and reporting

| Input / Variable | Description              | Default value                                     |
| -------------------------------------- | ------------------------ | ------------------------------------------------- |
| `sbom-image` / `MAVEN_SBOM_IMAGE` | The image used to perform and complete the Security Bill of Materials | `docker.io/anchore/syft:debug` |
| `sbom-opts` / `MAVEN_SBOM_OPTS` | SBOM options to complete the Security Bill of Materials  | `--override-default-catalogers rpm-db-cataloger,alpm-db-cataloger,apk-db-cataloger,dpkg-db-cataloger,portage-cataloger,nix-store-cataloger,java`          |
| `trivy-image` / `MAVEN_TRIVY_IMAGE` | The image to perform container security scanning  | `docker.io/aquasec/trivy:latest` |
| `trivy-args` / `MAVEN_TRIVY_ARGS` | Additional [`trivy image` options](https://trivy.dev/docs/latest/references/configuration/cli/trivy_image/#options) | `--ignore-unfixed --pkg-types os --disable-telemetry --skip-version-check` |

Other Trivy parameters shall be configured using [Trivy environment variables](https://trivy.dev/docs/latest/references/configuration/cli/trivy_image/#options).
Examples:

* `TRIVY_SEVERITY`: severities of security issues to be displayed (comma separated values: `UNKNOWN`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`)
* `TRIVY_SERVER`: server address (enables client/server mode)
* `TRIVY_DB_REPOSITORY`: OCI repository to retrieve Trivy Database from
* `TRIVY_JAVA_DB_REPOSITORY`: OCI repository to retrieve Trivy Java Database from

##### Jib build and publish configuration

Tho `mvn-build` job produces and uploads the container snapshot to the registry provided in `$MAVEN_JIB_SNAPSHOT_IMAGE` via the Jib `build` goal, e.g., `mvn verify com.google.cloud.tools:jib-maven-plugin:build`.

Publishing the release image follows the two-phase Maven release and deploy model. The `mvn-release` job is responsible for versioning and tagging 
the `pom.xml` using the Maven Release Plugin, e.g., `release:prepare`. The `mvn-deploy-release` job deploys, or "releases," the container via [`skopeo copy` arguments](https://github.com/containers/skopeo/blob/main/docs/skopeo-copy.1.md) to the provided registry in `$MAVEN_JIB_RELEASE_IMAGE`.

| Input / Variable | Description                                                | Default value     |
| --------------------------------- | ---------------------------------------------------------- | ----------------- |
| `skopeo-image` / `MAVEN_SKOPEO_IMAGE` | The image used to publish docker image with Skopeo         | `quay.io/containers/skopeo:latest` |
| `jib-build-args` / `MAVEN_JIB_BUILD_ARGS` | [Jib Maven Plugin arguments](https://github.com/GoogleContainerTools/jib/tree/master/jib-maven-plugin#extended-usage). | `-Djib.to.image=$MAVEN_JIB_SNAPSHOT_IMAGE` |
| `jib-publish-args` / `MAVEN_JIB_PUBLISH_ARGS` | Additional [`skopeo copy` arguments](https://github.com/containers/skopeo/blob/main/docs/skopeo-copy.1.md), e.g., `--additional-tag=strings`  | _none_ |
| `jib-prod-publish-strategy` / `MAVEN_JIB_PROD_PUBLISH_STRATEGY` | Defines the publish to production strategy for `mvn-release` and `mvn-deploy-release` jobs. One of `none`, `auto`, `manual`.   | `manual` |

#### Usage

See the Jib [Quickstart](https://github.com/GoogleContainerTools/jib/tree/master/jib-maven-plugin) 
for minimal guidance on the use of the plugin for your project. If you're here, you probably have a use case, 
i.e., you kicked off a [JHipster](https://jhipster.tech/) project and found Jib pre-configured for containerization.

The template uses GitLab registries and authentication defaults. See the Docker template for configuring alternate [registries and credentials](https://gitlab.com/to-be-continuous/docker#registries-and-credentials).

`$MAVEN_JIB_BUILD_ARGS` sets the snapshot container publish registry via a System Property, `-Djib.to.image=$MAVEN_JIB_SNAPSHOT_IMAGE`. This can be declaratively provided in the POM configuration for the Jib plugin and omitted, e.g., `#MAVEN_JIB_BUILD_ARGS` or `$MAVEN_JIB_BUILD_ARGS: ""` in the project `.gitlab-ci.yml`. 
This is advanced usage and should be understood in context of how `skopeo copy` works in the production pipeline.

#### Registry authorization

The variant tooling, Jib and Skopeo, support [Docker configuration files (default)](https://github.com/GoogleContainerTools/jib/tree/master/jib-maven-plugin#using-docker-configuration-files). 
Jib supports additional authentication methods, including [credential helpers](https://github.com/GoogleContainerTools/jib/tree/master/jib-maven-plugin#using-docker-credential-helpers), 
[the POM and CLI](https://github.com/GoogleContainerTools/jib/tree/master/jib-maven-plugin#using-specific-credentials), 
and [even Maven Settings](https://github.com/GoogleContainerTools/jib/tree/master/jib-maven-plugin#using-specific-credentials), e.g., `.m2/settings.xml`. 

All authentication methods should use masked GitLab environment variables.

#### Example

```yaml
include:
  # main template
  - component: $CI_SERVER_FQDN/to-be-continuous/maven/gitlab-ci-maven@5.4.0
  # Jib is implemented as an extension to Maven, and uses supporting features of the TBC Maven template
  - component: $CI_SERVER_FQDN/to-be-continuous/maven/gitlab-ci-maven-jib@5.4.0
```

### Vault variant

This variant allows delegating your secrets management to a [Vault](https://www.vaultproject.io/) server.

#### Configuration

In order to be able to communicate with the Vault server, the variant requires the additional configuration parameters:

| Name              | Description                            | Default value     |
| ----------------- | -------------------------------------- | ----------------- |
| `TBC_VAULT_IMAGE` | The [Vault Secrets Provider](https://gitlab.com/to-be-continuous/tools/vault-secrets-provider) image to use (can be overridden) | `registry.gitlab.com/to-be-continuous/tools/vault-secrets-provider:master` |
| `VAULT_BASE_URL`  | The Vault server base API url          | **must be defined** |
| `VAULT_OIDC_AUD`  | The `aud` claim for the JWT | `$CI_SERVER_URL` |
| :lock: `VAULT_ROLE_ID`   | The [AppRole](https://www.vaultproject.io/docs/auth/approle) RoleID | _none_ |
| :lock: `VAULT_SECRET_ID` | The [AppRole](https://www.vaultproject.io/docs/auth/approle) SecretID | _none_ |

By default, the variant will authentifacte using a [JWT ID token](https://docs.gitlab.com/ci/secrets/id_token_authentication/). To use [AppRole](https://www.vaultproject.io/docs/auth/approle) instead the `VAULT_ROLE_ID` and `VAULT_SECRET_ID` should be defined as secret project variables.

#### Usage

Then you may retrieve any of your secret(s) from Vault using the following syntax:

```
@url@http://vault-secrets-provider/api/secrets/{secret_path}?field={field}
```

With:

| Name                             | Description                            |
| -------------------------------- | -------------------------------------- |
| `secret_path` (_path parameter_) | this is your secret location in the Vault server |
| `field` (_query parameter_)      | parameter to access a single basic field from the secret JSON payload |

#### Example

```yaml
include:
  # main template
  - component: $CI_SERVER_FQDN/to-be-continuous/maven/gitlab-ci-maven@5.4.0
  # Vault variant
  - component: $CI_SERVER_FQDN/to-be-continuous/maven/gitlab-ci-maven-vault@5.4.0

variables:
    # Vault configuration
    VAULT_OIDC_AUD: "https://vault.acme.host"
    VAULT_BASE_URL: "https://vault.acme.host/v1"
    # Secret managed by Vault
    SONAR_PASSWORD: "@url@http://vault-secrets-provider/api/secrets/sonar?field=password"
```
