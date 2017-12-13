# Ansible Playbooks and Roles

From me [@mrlesmithjr](https://www.twitter.com/mrlesmithjr) to the community. I
have put together this repo to be a single collection of all my `Ansible` roles.
This could have many usages such as a single repo collection for learning. Hope
you enjoy!

> NOTE: This repo will always be updated on a continuous basis and all feedback is
> encouraged and welcomed.

## Notes

All of my roles can be found in `roles/`. The `roles.old/` folder is for historical
purposes.

## Updating Roles

To ensure all roles are current and up to date you can run the following in
the root of this repo..

```bash
ansible-galaxy install -r requirements.yml -f -p ./roles --ignore-errors
```

## License

MIT

## Author Information

Larry Smith Jr.

-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   mrlesmithjr [at] gmail.com
