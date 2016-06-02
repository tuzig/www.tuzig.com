Title: Freeing a Yuck
Author: Benny Daon
Date: 2016-06-03 01:00
Category: Blog


    
    ***Mazal Tov to Alon for the birth Nizan and Ruth***

    Written as reply to Alon Nisser post:  "I toggled public now what?"

A couple of weeks ago, that I walked into Dan's office for a chat.
We've talked about what we should do next, now that we've completed
opening the legacy DB with an API. Dan called it getting our Yack on the truck
and it freaked me.

Imagine, finding yourself driving a truck with a poor Yuck at the back cage
with no idea where you're going.

![Wild Yack](/images/wild_yack.jpg)

Not only that, you feel the Yack is visited by more people and it becomes the
center piece in many conversations and presentation.
It behaves so well, It's temting to forget it's is still a wild beast,
with tons of bugs and very few tests. I'm sure the beast can - and probably will -
kick me in the head.

Not only that, the Yack has a *Bus Factor* of just one, yours truly,
so I stopped the truck and starting working on the locks to free the beast.

I wrote a README, chose a license and pushed the repo to github
(we were using bitbucket before).

The license is critical as it establishes the relationships between
the contibutors and the copyright holder. I prefer the 3-clause BSD license of
Django, as it's very short - 27 lines- and free,
but this time around it didn't feel right.

![Linus Finger](https://cdn.meme.am/instances/400x/22157430.jpg)

I ended up choosing the dreaded Aferro GPLv3, a lengthy legal doc, just 5 lines
short of the number of the beast.  I once met the author,
St IGNUcius of the Church of Emacs, and asked him if there was no way to
make it shorter.  It made him angry. HOORAY!

Imagine myself, a humble worshiper of sed's visual mode, poking a finger in
the eye of that pompus emacs user.  St. my arse.

Anyways, I picked his license, as at the end of the day, the copyright holder
will never be a kniving corporation. The Museum is an Israeli Non profit founded in 1978 and
there is no chance it will fall into the hands of some greedy lawwyers that
will sue contributors, so the license is not that important.

[I toggled public. Now what?](https://medium.com/@alonisser/i-toggled-public-now-what-6b42959db251A).


Next came a pull request from Alon that helped me with that dman grunt (I know,
gulp is better, if you can help, [feel free to fork](https://github.com/Beit-Hatfutsot/dbs-front) )

Next, alon shared with me his post.  In it I found a bug:  the
default API server is localhost:5000 which no one except Inna and Myself have,
as we didn't release the backend code yet.

I changed the default to our test server in devapi.dbs.bh.org.il and started
working with Niko on getting the issues over from the Jira Hell.
We now have 77 open issues and six closed so far. We also have a couple of milstones and the next one even has a deadline in 10 days.

I'm not yet sure what the open source community is getting from all of this
and I don't care. It's been great for the team and for now, that's all that  matters.
