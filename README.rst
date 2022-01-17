aicoe-hello-world
-----------------

A small example demonstrating Python package releases uploaded using AICoE-CI
to `Operate First Pulp instance
<https://www.operate-first.cloud/community-handbook/pulp/usage.md>`__.

How To
======

To trigger a new package release to Pulp:

1. Make sure you are stated as a maintainer of the package in ``.thoth.yaml``
   file (in "version" manager section)

2. Trigger a new release by opening an issue - follow `Kebechet version manager
   documentation for more info
   <https://github.com/thoth-station/kebechet/tree/master/kebechet/managers/version#kebechet-version-manager>`__

3. Once the PR is opened and all CI checks pass, the pull request adjusting
   version identifier is automatically merged

4. The pipeline will release the Python package to the Pulp instance,
   respecting ``.aicoe-ci.yaml`` configuration present in Git root

  * To check progress, visit `Tekton on Operate First (PipelineRuns)
    <https://tekton.operate-first.cloud/#/namespaces/opf-ci-pipelines/pipelineruns>`__
    and in the search bar type: ``project:<github-project-name>`` (e.g.
    ``project:aicoe-ci-pulp-upload-example``)
