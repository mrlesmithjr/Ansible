Role Name
=========

Clone a Users Git Repo in full.

Requirements
------------

Define a user in defaults/main.yml to clone all of their repos from.

I created this as I had a need to ensure that all of my GitHub repos were always cloned locally and in-full. I also wanted a way to have the ability to update and commit changes from the cloned destination In order to do this you must have SSH Keys added to the Users repo in which you want to make changes to. Also allows adding additional GitHub users to github_users variable to pull others repos as well :)

Role Variables
--------------

````
---
# defaults file for ansible-clone-git-repos
github_repo_root: ~/Git_Projects/GitHub  #define destination to store GitHub repos to be cloned
github_users:  #define github user(s) to clone repos from and define pages to ensure all repos are gathered.
  - user: bunchc
    pages:
      - 1
  - user: debops
    pages:
      - 1
      - 2
  - user: lowescott
    pages:
      - 1
  - user: Mierdin
    pages:
      - 1
  - user: mrlesmithjr
    pages:
      - 1
      - 2
  - user: dstamen
    pages:
      - 1
  - user: phpipam
    pages:
      - 1
repos_file: ../vars/git_repos.yml  #leave this as-is
return_items: 100  #defines the number of items to return per-page on the uri API call to GitHub....This equates to the number of repos.
````

Execution
---------
After defining the users name in defaults/main.yml you can execute the script that will do everything for you.
````
./clone_git_repos.sh
````

Dependencies
------------

None

Notes
-----
This is very rough at this time and only defined with using GitHub. More functionality may or may not be added. Time will determine this. I also created this to possibly use in an automated fashion to clone repos and such. Maybe using Jenkins :) This was all created as a role layout in prepartion of more to come which may leverage this as an actual role.


License
-------

BSD

Author Information
------------------

Larry Smith Jr.
- @mrlesmithjr
- http://everythingshouldbevirtual.com
- mrlesmithjr [at] gmail.com
