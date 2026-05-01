Jai Jagannath
There a CRM system that has almost all the details that are required for the Fidelitus Corp MD Dashboard.

The overall flow is something like this. The MD logs in and his landing page show the following at a corporate level that is a consolidation of all his companies.

Target for year
Revenue I.e booking achieved
Invoiced amounts
Payments made
Meetings done
Proposals submitted

All these have numbers and values.

Also the following are shown
1. Delta from  previous meeting weekly
Committed vs actual for each of these above shown right next the above goals and values and numbers.
Now each of these number and values commited in the last week vs actuals achieved wil have bright red if less than 25% taget is met
Red is between 26% - 50%, 51-75% would be orange and green if 75% is met.

Below it are boxes for each of the companies that show the same outlined below the companies  but for their specific company.  Each of them are boxed with a small button to know more.

The companies are
Fidelitus Transactions
Fidelitus projects
Fidelitus FMS
Fidelitus HR labs
Fidelitus Technology
Fidelitus GCC Nexus

The details are as follows
Target for year
Revenue I.e booking achieved
Invoiced amounts
Payments made
Meetings done
Proposals submitted
lso the following are shown
1. Delta from  previous meeting weekly
Committed vs actual for each of these above shown right next the above goals and values and numbers.
Now each of these number and values commited in the last week vs actuals achieved wil have bright red if less than 25% taget is met
Red is between 26% - 50%, 51-75% would be orange and green if 75% is met.
If MD clicks on more than aging analysis of these values that are delayed from commited week is shown as 7 day, 14, day, 21 days, 90 days and then as NPA if 
beyond 90 days. He can then click on these and the details of each of those is shown in terms of which company , team member and any details
that the team member of the company has entered as reason.

 


Also right below this are the following
details of leads generated from Corp. These are leads that have been passed on by the MD or the corporate team.
Leads
Meetings
Proposals
Orders
Invoices
Collections

Each of them should have delta of targets vs actuals from last week 
Again here Now each of these number and values commited in the last week vs actuals achieved wil have bright red if less than 25% taget is met
Red is between 26% - 50%, 51-75% would be orange and green if 75% is met.
If MD clicks on more than aging analysis of these values that are delayed from commited week is shown as 7 day, 14, day, 21 days, 90 days and then as NPA if 
beyond 90 days. He can then click on these and the details of each of those is shown in terms of which company , team member and any details
that the team member of the company has entered as reason.

The production is actual shown in the first few ( whatever you decide ) as a mocks up with values contrived for 
getting the MD to accept the flow.

But if you carefully look thru the directory we have the actuals values except probably for targets available in the mongodb. Those hooks should
be created as subsequent sessions which my developer will run as as I dont know the eact schema. Also the first
mockup there is no login but the actual production code and mongodb have all that embedded into the CRM. He will have to
integrate those and any other components that he has developed to show the values being shown are what is 
there in the DB and not the mockup. Maybe he sets a flag in the env file production = 0 ( actual ) and 1 for mockup.

Please add and modify anything else that you wish that may moake sense to a MD of a group holding companny. 
Keep graphics as light as possible. Clear and disticnt, nothing fancy
Jai Jagannath