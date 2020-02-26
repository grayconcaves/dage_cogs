# How to use Ao3

This ao3 cog grabs info from an Ao3 work link and compiles it into a discord message.

__Usage:__ `[p]ao3 <link> <optional: notes>`

## Admin Commands
Server admin and owners can take full advantage of this cog's customizable features.


### **ao3set**
__Usage:__ `[p]ao3set`

Shows all the customizable features, which include:

 - **autodelete** toggles if the bot automatically deletes the message that called it. Default is FALSE. The bot needs Manage Messages permissions if this set to TRUE.
 
 - **censor** toggles if an Explicit work's tags will be automatically censored/spoilered. Default is TRUE.

 - **embeds** toggles if the work info will show as a preset embed or customizable text. Default is FALSE.
 
 - **fandom <number>** sets a maximum number of fandom tags.
 
 - **pairs <number>** sets a maximum number of relationship tags.

 - **tag <number>** sets a maximum number of additional tags.


### **ao3format**
__Usage:__ `[p]ao3format <custom format or RESET>`

Embeds need to be set as FALSE. This allows you to customize the info card that the bot will send. To return to default formatting: `[p]ao3format RESET`


### **formathelp**
__Usage:__ `[p]formathelp`

This shows how to make a custom format to be used for **ao3format**. 

You can use the following parameters for your ao3 info:
`url, title, authors, rating, warnings, language, fandom, pairing, tags, summary, totalchapters, status, words, notes, reccer`

To format the message with these parameters, include them in your message encased in curly braces {}

You can also add whitespace (using Shift+Enter) as well as use Discord's native formatting.
        
For example:
```[p]ao3format
**{title}** by {authors}.
Pairing: {pairing}
Rating: {rating}
Tags: {tags}
Summary: 
{summary}
```

Result after using `[p]ao3 <link>`:
```**Title** by Author.
Pairing: Pairing(s)
Rating: Rating
Tags: Tag 1, Tag 2, Tag 3, Tag 4, Tag 5
Summary:
summary
```

To see your current formatting: `[p]formathelp current`
To see the default formatting: `[p]formathelp default`

## Automating Ao3

To emulate the **Fanfic Rec Bot**, I recommend using this with Trusty-cogs [**retrigger**](https://github.com/TrustyJAID/Trusty-cogs/tree/master/retrigger) for it to automatically detect if an ao3 link has been used.

`[p]retrigger command ao3 (?:(?=https://archiveofourown.org/works))(.*) ao3 {1}`

Then you can restrict the channels where it does this automatically.

`[p]retrigger whitelist add ao3 <#channel>`

__Note:__ Please remember that this will work even if words were used before the link. However, you still need to put any reccer's notes **after the link** for them to be detected. Any words before the link will not be detected by the cog.

