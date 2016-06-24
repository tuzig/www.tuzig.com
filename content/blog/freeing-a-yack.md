Title: Freeing a Yuck
Author: Benny Daon
Date: 2016-06-03 01:00
Category: Blog

# Freeing a Yack

[ Written as reply to [Alon Nisser](https://medium.com/u/2a5400d58707) post: "[I toggled public, now what?](https://medium.com/@alonisser/i-toggled-public-now-what-6b42959db251#.e8vt352qf)" ]  

A couple of weeks ago, I walked into the CEO's office for a chat.  
We've talked about what we should do next, now that we've completed opening the legacy DB with an API. Dan called it getting our Yack on the truck and it freaked me.


![A Wild Yack](https://cdn-images-1.medium.com/max/800/1*z5udGDTt7uL5VINRClZLdw.jpeg)

Imagine, after a lot of pushing and shoving, finally you got the wild yack on the track and you're driving a truck with a poor Yack at the back cage and with no idea where you're going.  

Not only that, you feel the Yack is visited by more people and it becomes the center piece in many conversations and presentation. It behaves so well, It's tempting to forget it's is still a wild beast, with tons of bugs and very few tests. I'm sure the beast can - and probably will - kick me in the head.  

Not only that, the Yack has a **Bus Factor** of just one, yours truly, so I hit the breaks and start working on the locks to free the beast. I wrote a README, chose a license and pushed the repo to github (we were using bitbucket before).  

Usually, the license is critical as it establishes the relationships between the contributors and the copyright holder. If it was my choise, I'd pick the 3-clause BSD license of Django, as it's very short - 27 lines- and free, but this time around it didn't feel right.  

I ended up choosing the dreaded Aferro GPLv3, a lengthy legal doc, just 5 lines short of the number of the beast. I once met its author, St IGNUcius of the Church of Emacs, and asked him if there was no way to make it shorter. It made him angry. HOORAY! (Imagine myself, a humble worshiper of sed's visual mode, poking a finger in the eye of that pompous emacs user)  

Anyways, I picked his license, as at the end of the day, The Museum is an Israeli Non profit founded in 1978 and there is no chance it will fall into the hands of some greedy lawyers that will decide to take the code private or sue contributors. IMHO, when you're sure the copyright holder will never be a kniving corporation, the license is not that important.  

##So I toggled public.

Next came a pull request from Alon that helped me with that damn grunt (I know, gulp is better, if you can help, [feel free to fork](https://github.com/Beit-Hatfutsot/dbs-front)).  

Next, Alon shared with me his post. In it I found a bug: the default API server is localhost:5000 which no one except Inna, my co-developer, and Myself have, as we didn't release the server code yet.  

I changed the default to our test server in devapi.dbs.bh.org.il and as Alon requested, started working with Niko (QA) and Nurit (the boss) on getting the issues over from Jira Hell.

As of now we have 61 open issues and 31 we already closed. We also customized the labels a bit and have a couple of Milestones we use to prioritize issues.  

I'm not yet sure what the open source community is getting from all of this and frankly, I don't really care. It's been great for the team and for now, that's all that matters.
