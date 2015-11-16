# When returning from vacation, you have to delete some unwanted email messages in your inbox, like spam or
# other unimportant messages. Your inbox consists of several pages that each contain the same number of
# messages (except possibly the last page). Each message has two corresponding buttons that allow you to:
#  - add the message to the current selection
#  - remove the message from the current selection
#
# In addition, each page has three buttons with the following functions:
#  - select all messages on the current page
#  - delete all selected messages on the current page
#  - advance to the next page of messages (unless you're already on the last page)
#
# Selections do not extend across pages, and advancing to the next page deselects everything that is currently
# selected. Also, deleting messages will not cause later messages in the inbox to scroll up to the current page.
#
# For example if you have four email messages on one page and you would like to delete the second one, you could
# select it and then click on delete for a total of two clicks. An alternative is to select all messages, then
# deselect all other messages except the second, and then click delete, for a total of five clicks.
#
# Naturally, you would like to clean up your inbox with as few clicks as possible. Furthermore, you are allowed
# to choose the number of emails to display per page. If you decide to display K messages per page, the first K
# messages will be on the first page, the next K messages will be on the second one, and so on. Obviously, the
# last page might contain less than K messages. Note that you need to check all pages of messages, even if they
# do not contain any messages that must be deleted.
#
# You will be given a string messages containing a description of email messages in the order they appear in your
# inbox. The 'D' character denotes a message that should be deleted, while a '.' character denotes an email that
# should be kept. You will also be given two integers, low and high, denoting the inclusive lower and upper bounds
# of the number of messages on each page. You should choose how many emails to display per page such that the number
# of clicks needed is minimal, and then return the number of clicks.

import sys
import math

class InboxCleanup:
	def fewestClicks(self, messages, low, high):
		#print(messages,low,high)
		best = (0, sys.maxsize)
		for pageSize in range(low, high + 1): # for each possible page size
			clicks = 0
			page = 0
			while page*pageSize < len(messages):
			#for page in range(0, (len(messages) // pageSize + 1)):
				messagesOnPage = messages[page*pageSize:(page+1)*pageSize]

				deleteCount = messagesOnPage.count('D')
				keepCount = len(messagesOnPage) - deleteCount

				markForDelete = True
				anyMarkedForDeletion = False
				if deleteCount > keepCount:
					#print('select all')
					clicks += 1 # select all for deletion
					markForDelete = False # mark the messages that shouldn't be deleted
					anyMarkedForDeletion = True

				for messageIdx in range(0, len(messagesOnPage)): # for each message
					if markForDelete and messagesOnPage[messageIdx] == 'D':
						#print('select (' + str(page) + ', ' + str(messageIdx) + ')')
						clicks += 1 # mark message for deletion
						anyMarkedForDeletion = True
					elif not markForDelete and messagesOnPage[messageIdx] == '.':
						#print('deselect (' + str(page) + ', ' + str(messageIdx) + ')')
						clicks += 1 # unmark message for deletion

				if anyMarkedForDeletion:
					#print('delete all selected')
					clicks += 1 # delete all selected

				#print('next page')
				clicks += 1 # move to next page
				page += 1

			clicksFinal = clicks - 1
			#print('final (' + str(pageSize) + ', ' + str(clicksFinal) + ')')
			if clicksFinal < best[1]: best = (pageSize, clicksFinal)
		return best[1]

print(InboxCleanup().fewestClicks('..........', 5, 10))
print(InboxCleanup().fewestClicks('.D.D.DD.D.', 5, 5))
print(InboxCleanup().fewestClicks('...D..DDDDDD...D.DD..', 3, 10))
print(InboxCleanup().fewestClicks('D.D..D..DD.DDDD.D.DDD.DDDD..', 3, 11))
print(InboxCleanup().fewestClicks('DDD.........................', 3, 3))
