# RugbyLug Project 2: Mycroft-Todo

Mycroft skill to manage a todo.txt

## Background

During the July social, we discussed many candidates for a Mycroft skill project but felt that the most useful would be a check-list / Todo list skill as it seems more achievable in a short time.

## Objectives & success criteria

This project will be considered a success when the following have been achieved:
1. The skill has sufficient language processing skills to be useful to an untrained and non-technical person
1. That the 'database' is stored in the standaterd Todo.txt format
1. That entries can be added, read, amended, removed (CRUD: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

Any others?

## Implementation

An existing project (The Cows Lists) was identified that has similar aims (https://github.com/CarstenAgerskov/skill-the-cows-lists) but that uses a REST interface to the 'Remember The Milk' online service (requires user account). As there is a general lean toward privacy, saving personal data on an on-line 'free' service is unlikely to be adopted by the members of our group and I am sure this also goes for others.

As a backend, we considered using a plan text based task list format, for example Todo.txt  (https://github.com/todotxt/todo.txt) More info here: https://www.howtogeek.com/355890/every-to-do-list-app-sucks-switch-to-todo.txt-instead/.

This will need to be stored somewhere if it is to be accessed from multiple locations. Persistent storage could be created using a Git sync or Webdav. Nextcloud could be used for a private store via Webdav as detailed here: https://github.com/EpocDotFr/webtodotxtor and Nextcloud already has a native Todo.txt app (https://play.google.com/store/apps/details?id=nl.mpcjanssen.simpletask.nextcloud).

If The Cows Lists seems to be on the lines of what we want, it could be re-factored or improved instead of starting from scratch but with an alternative integrated back-end and improved language.

Mycroft have a quality process (https://mycroft.ai/documentation/skills/skills-acceptance-process/) which we should be aware of if we want any work to be adopted by the wider Mycroft community.

A regular contributor has posted a blog (https://geekedoutsolutions.com/mycroft-skill-creation-lifecycle-using-msk) to help developers get started when creating a new skill.

It might be worth adding that there is a related web site http://todotxt.org

That has links to a boat-load of community applications, as well as its own:
- GPL 3 shell-script based CLI (https://github.com/todotxt/todo.txt-cli), 
- GPL 3 Android app (https://github.com/todotxt/todo.txt-android) and 
- GPL 3/MIT iOS app (https://github.com/todotxt/todo.txt-ios)
(NB the links in http://todotxt.org to the Android and iOS apps are broken, I found them via https://github.com/todotxt)

Somewhat elegantly the Android app gets replication across devices by keeping the todo.txt file in dropbox. (So I assume that should be fixable.)

I assume the CLI can be easily be configured to do the same, but I haven't checked.

I think that local storage would be the best place to start so that we don't get hung up with integrating to another service.

I've stumbled across two other links that we may find useful.

There is already a Todotxt implementation in python https://pypi.org/project/todopy/ . I've not tested or used it so can't comment on it's completeness.

There is also a Todo app integrated with Todoist https://github.com/gerlachry/skill-todoist. We could perhaps look at extending this or using it as a basis for our skill.

