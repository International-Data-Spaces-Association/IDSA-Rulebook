# Contributing to IDSA Github

This is the woring repository of [IDSA](https://www.internationaldataspaces.org) Working Group Rulebook.

All issues and pull request need to be discussed in the Working Group meetings.

All content published here is provided and approved by the Working Group Rulebook. You are very welcome to contribute to this repository when you find a bug, want to suggest an improvement, or have an idea for a useful feature. For this, always create an issue and a corresponding branch, and follow our style guides as described below.

Please note that we have a [code of conduct](CODE_OF_CONDUCT.md) that all contributors should stick to.

## Issues

You always have to create an issue if you want to propose a correction, improvement, or feature.
Briefly and clearly describe the purpose of your contribution in the corresponding issue.
The pre-defined [labels](#labels) improve the understanding of your intentions and help to follow
the scope of your changes.

## Labels

The [labels](https://github.com/International-Data-Spaces-Association/idsa/labels) are listed at the
[issues](https://github.com/International-Data-Spaces-Association/idsa/issues).
There are two types of labels: one describes the content of the issue and should be used by the
developer that creates the issue. The other one, starting with `status`, will be added from the
developer that takes on the issue. New issues should be initially marked with `status:open`.

* Basic labels: `bug`, `documentation` `duplicate`, `enhancement`, `good first issue`, `help wanted`, `invalid`, `question`, `wontfix`
* `bug`: Something isn't working
* `documentation`: Improvements or additions to documentation
* `duplicate`: This issue or pull request already exists
* `enhancement`: New feature or request
* `good first issue`: Good for newcomers
* `help wanted`: Extra attention is needed
* `invalid`: This doesn't seem right
* `question`: Further information is requested
* `wontfix`: This will not be worked on

## Branches

After creating an issue yourself or if you want to address an existing issue, you have to create a
branch with a unique number and name that assigns it to an issue. Therefore, follow the [guidelines](https://deepsource.io/blog/git-branch-naming-conventions/).
Make your changes in your branch, invite others to collaborate on those changes.
Then, create a pull request and note that **committing to the main branch is not allowed**. Please use the feature `linked issues` to
link issues and pull requests.

Pull requests have to be approved by 2 reviews from either the IDSA Head Office or the Working Group Leads.

## Commits

We encourage all contributors to stick to the commit convention following the specification on
[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). In general, use  the imperative in the present tense.

## Figures

Please be aware that figures with a transparent background are displayed differently when the user decides to use the dark or the light mode.
Figures should always use a non transparent background.

## Versioning

The IDSA Rulebook follows a release approach based on the approval of the IDSA Working Group Rulebook. The versioning follows the scheme 'year-sequence - YYYY-N', e.g., 2026-1 for the first release in 2026.

Older releases can be found on in the IDSA GitHub repository knowledge base.

## Non-linear layout

The IDSA Rulebook is a non-linear document. Sections should reference other sections as needed and link to those referenced sections.

Each topic of the IDSA Rulebook shall be created in its own file for easier linking and asynchronous updating. Additional new topics can be added.

Please, pay attention to update the the [Readme.md](README.md), as well as [Summary.md](SUMMARY.md) if you add additional topicss or remove existing ones. When removing existing ones, please, check for broken references in other files.
