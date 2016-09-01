Title: A Museum's First Hackathon
Author: Benny Daon
Date: 2016-09-01 11:59
Category: Blog

It's been an interesting first year of freelancing at The Museum of
The Jewish People.  I wrote a lot of code, released quite a few versions
and met some very good people.

Together we've opened some of the code of our databases site, published an
[API](http://devapi.dbs.bh.org.il/v1/docs) and started
using creative commons licenses. We're now probably the most advanced Museum
in Israel when it comes to digital assets and we keep pushing that envelope.

So when I met Daphne in a *Django Girls* meetup and heard about HackExtend
I offered to help and make it happen at the Museum.

## AND IT'S HAPENING!

In a fortnight, at the 15-16/9/2016, I'll be hacking in the first ever
HackExtend right here, at Beit-Hatfutsot - The Museum of The Jewish People - and the hit is on.  The Museum's have put a lot of time into this and I have to prove
It's worth it, so we can have many more Hackathon's at our excellent
facilities - two auditorion with 100 & 200 seats, 10 class rooms and the gardens
of Tel Aviv University.

My original plan was to prepeare a lot of [beginner issues](https://github.com/Beit-Hatfutsot/dbs-front/labels/beginner) and help people
install the enviornment, pick an issue, fix it and submit a pull request.
It's all very nice but after the pre-hackathon meetup last firday,
I understood these tasks don't fit those that are a part of a team as teams
need a project.  So we've banged our heads together and came with four small
projects that are we'd love to have and are fun to develop.

Here they are for your consideration,  ordered from the dullest to the coolest:

### Admin Interface

We have registered users and we have roles, but no way to manage them.
When I need to make someone an *editor* I have to launch the python shell on
the server and run a couple of commands.  While it's been fun playing with the
shell, we can really use and Admin interface to manage users and roles.

This project needs a bit of UX design, frontend (prefrebbly angular 2) and some
backend (flask-user).

### My Story revamp

We have a section on the site where registered users can collect items
, group them in branches and share them with the world. It works - 
here's [my story](http://test.dbs.bh.org.il/story/2e775e50cffbe657e7179569822f002b)
- but it needs some serious face lifting.

We need to name branches automaticly based on the Place & Family the user searched for.
Good branch names will allow us to improve our 'Related' links which are now
terrible (based on elasticsearch's more-like-this feature) as we can find
related items in users' branches i.e. For 'Paris' the related items are
those that appear in more then one branch named *Paris*.

At the display front, we need to let the user control the order of the
cards - i.e. put my grandmother's card first - and posiibly over their size.
It'll also be nice to let users customize as much of the display as possible -
many of the users will be kids, researching their family roots, and they
love customizing.

And we need to make it easier to put items directly into the branch I'm
currently researching.

This project needs UX design and angular 1.4 coding on our frontend.  Netta, our
resident designer, will help, explaining UI guidelines and sharing photoshop
files.

### Family Tree Creator

So far we've only developed a *read* interface to the family trees and users
are demanding a way to create and edit trees.  A Creation interface is simpler
so we want to focus on that as the first step, allowing registered users to 
create their own tree.

The challenge here is to use the interface you develop to create a complex tree,
like [the one from Genesis](https://he.wikipedia.org/wiki/%D7%AA%D7%91%D7%A0%D7%99%D7%AA:%D7%90%D7%99%D7%9C%D7%9F_%D7%99%D7%95%D7%97%D7%A1%D7%99%D7%9F_%D7%A9%D7%9C_%D7%93%D7%9E%D7%95%D7%99%D7%95%D7%AA_%D7%A1%D7%A4%D7%A8_%D7%91%D7%A8%D7%90%D7%A9%D7%99%D7%AA).

### Visitors Visulaziation for the Physical World

At the entrance to the Museum we have a wall with 9 screens forming a 16:9
rectangle with a diagonal of 126 inches.  It currently shows clips from Jewish
Weddings and we want to replace it with a live world map of visitor to the site
and the content viewed.  The winning visualization will run on that wall and
will put a small plaque with the names of the team members.

The logs are published using [google's pub/sub](https://cloud.google.com/pubsub/docs/overview) service and ip to geo seems straight forward enough -  I installed locally [freegeoip](https://github.com/fiorix/freegeoip) and it works like a charm.

This will require some creative UX/UI design, simple backend and a small webapp,
prefreablly using angular 2.

# See you at HackExtend!


