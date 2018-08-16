# Mycroft Todo skill

This skill provides a to-do list using the todotxt back-end. Therefore this does not rely on any 3rd parties or external services. The todotxt file is stored locally on the Mycroft and can be syncronised with tdotxt services including Nextcloud.

Initial code borrowed from https://github.com/gerlachry/skill-todoist (GPL 3 assumed)

Uses https://developer.todoist.com/?python#api-overviewapi APIs for creating tasks under a project.

## Requirements
* install todoist-python library to mycroft-core virtualenv
    * pip install todoist-python
* git clone to skill directory

## Language usage

The following language is planned but mostly not implemented. Items implemented are marked.

### Create a list 
- create a list called SOMELIST
   - {{listname}} created

### Set the default list (if more than one)
- set list as default
   - List {{listname}} set as default

### Use a list (if more than one)
- use list SOMELIST
   - Using list {{listname}}

### Find / check a list
- Find list SOMELIST
   - found list {{listname}}
   - cant find list {{listname}}

### Delete a list
- Remove list SOMELIST
   - Are you sure you want to remove list {{listname}}?
- yes
   - List {{listname}} removed

### Add an item to a list
- add {{item}} [to SOMELIST]
   - Item {{item}} added to {{listname}}

### Enumerate list
- How many items
   - There are  {{itemcount}} items on list {{listname}}

### Find an item
- Find item SOMEITEM
   - Item {{item}} found

### Set item priorty
- Make it priority 1
- Make it top priority
- Make it high priority
- Make it highest priority
- Make it low priority
   - Item {{item}} is now priority {{priority}}

### Set item target date
- Set due date to SOMEDATE
   - Item {{item}} due at {{duedate}}

### Set as complete
- mark as complete
   - Item {{item}} marked as complete

### Remove item
- Remove item SOMEITEM
   - Item {{item}} removed

### Get info on the item
- Tell me about it
   - Item {{itemname}} has priority {{priority}} and is due on {{duedate}}
