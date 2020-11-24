# Study Buddy
UVA - CS3240 - Fall 2020 - Advanced Software Development
#### Team 1-06: Members
* Requirements Manager - Caroline Chen (cc8tt)
* DevOps Manager - Kendall Livesay (krl7ee)
* Testing Manager - Noah Narciso (nn9ja)
* Scrum Master - Sarah Snow (ses9nd)

#### Overview
Study Buddy is a web application that allows users to find virtual study groups or partners. Users may upload profile information, search for specific members, create custom groups, or join an existing group. 

  - Users are able to log in to the site with an existing Google account. 
  - Users are able to save their course schedule with a comma-separated list. 
  - Course tags are automatically generated, allowing users to easily filter through the study groups.
  - Users are able to submit a custom bio that identifies the topics in which they are looking for additional support. 
  - Users are able to search for other members with similar schedules or interests. 
  - Users are able to form their own groups by identifying a name, topic, and intial list of group members. 
  - GroupMe groups are generated automatically.
  - GroupMe will display a custom welcome message and allow current group members to join.
  
#### User Profiles
The following information will be collected from users: 
  - Email (required)
  - Name
  - Bio
  - Graduation Year
  - Major
  - Computing ID
  - Course List

#### GroupMe
In order to maximize the functionality of the web application, it is recommended that users create a [GroupMe] account using their personal phone number. Study groups formed through the site will have the option to communicate via an automatically generated GroupMe group message. This is a way to virtually connect and communicate with other memebers about relevant coursework. The GroupMe groups will all have an admin account named StudyBuddy that is added to each group message. These groups will be unmonitored by default, but users can email the admin account studybuddy3240@gmail.com to report any malicious behavior.

#### Resources
StudyBuddy uses a number of open-source resources:

* [Bootstrap4]
* [Django]
* [Gunicorn]
* [django-allauth]
* [django-heroku]
* [django-taggit]

#### Acknowledgements
Thank you to Professor Sherriff, Professor McBurney, and our TA Kush Patel for helping us out this semester! We appreciate all the work that you've done to translate this course to a virtual environment. 

[//]: #
[GroupMe]: <https://web.groupme.com/>
[Bootstrap4]: <https://getbootstrap.com/>
[Django]: <https://www.djangoproject.com/>
[Gunicorn]: <https://gunicorn.org/>
[django-allauth]: <https://django-allauth.readthedocs.io/>
[django-heroku]: <https://devcenter.heroku.com/articles/deploying-python>
[django-taggit]: <https://django-taggit.readthedocs.io/>
[GroupyAPI]: <https://pypi.org/project/GroupyAPI/>
