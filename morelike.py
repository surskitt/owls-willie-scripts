from willie.module import rule
import re


@rule(r"(.*ay.*)")
def morelike(bot, trigger):
    msg = trigger.group(1)
    msg = re.sub(r"[^aeiou ]+ay", "GAY", msg)
    bot.say("More like " + msg)
