# Mycroft Todo skill

This skill provides a to-do list using the todotxt back-end. Therefore this does not rely on any 3rd parties or external services. The todotxt file is stored locally on the Mycroft and can be syncronised with tdotxt services including Nextcloud.

Project planning in the https://github.com/rugbylug/Mycroft-Todo/blob/master/BACKGROUND.md file.

Initial code borrowed from https://github.com/gerlachry/skill-todoist (GPL 3 assumed) and todoist code removed.

## Requirements
* pip install python-todotxt

* install library to mycroft-core virtualenv
* git clone to skill directory

## Language usage

The following language is planned but mostly not implemented. Items implemented are marked as such.

### Create a list :negative_squared_cross_mark:
- create a list called SOMELIST
   - {{listname}} created

### Set the default list (if more than one) :negative_squared_cross_mark:
- set list as default
   - List {{listname}} set as default

### Use a list (if more than one) :negative_squared_cross_mark:
- use list SOMELIST
   - Using list {{listname}}

### Find / check a list :negative_squared_cross_mark:
- Find list SOMELIST
   - found list {{listname}}
   - cant find list {{listname}}

### Delete a list :negative_squared_cross_mark:
- Remove list SOMELIST
   - Are you sure you want to remove list {{listname}}?
- yes
   - List {{listname}} removed

### Add an item to a list :white_check_mark:
- add {{item}} [to SOMELIST]
   - Item {{item}} added to {{listname}}

### Enumerate list :negative_squared_cross_mark:
- How many items
   - There are  {{itemcount}} items on list {{listname}}

### Find an item :negative_squared_cross_mark:
- Find item SOMEITEM
   - Item {{item}} found

### Set item priorty :negative_squared_cross_mark:
- Make it priority 1
- Make it top priority
- Make it high priority
- Make it highest priority
- Make it low priority
   - Item {{item}} is now priority {{priority}}

### Set item target date :negative_squared_cross_mark:
- Set due date to SOMEDATE
   - Item {{item}} due at {{duedate}}

### Set as complete :negative_squared_cross_mark:
- mark as complete
   - Item {{item}} marked as complete

### Remove item :negative_squared_cross_mark:
- Remove item SOMEITEM
   - Item {{item}} removed

### Get info on the item :negative_squared_cross_mark:
- Tell me about it
   - Item {{itemname}} has priority {{priority}} and is due on {{duedate}}
