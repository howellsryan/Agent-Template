# External companions

`systematic-debugging` and `verification-before-completion` come from
[obra/superpowers](https://github.com/obra/superpowers/tree/main/skills).
`test-driven-development` is also required by systematic-debugging.
The engineering profile pins all three. Their implementations remain upstream. They are not included in this plugin.

Repository bootstrap users declare exact upstream commit SHAs and selected skill
paths in `.agents/skills.lock.json`. The installer exposes the complete skill
directories, including supporting resources, from the pinned upstream checkout.
The upstream LICENSE stays in that checkout.

Native plugin users install the upstream Superpowers plugin separately using its
installation guide. If required companions are unavailable, report the missing
dependency and use the repository's documented bootstrap or explicit read path;
do not claim to have invoked a skill that was not loaded.
