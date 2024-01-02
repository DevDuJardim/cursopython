#magicians = ['alice','david','mr m']
#for magician in magicians:
 #   print(magician)

#magicians = ['alice','david','mr m']
#for magician in magicians:
#   print('{}, that was a great trick!'.format(magician.title()) )

magicians = ['alice','david','mr m']
for magician in magicians:
   print(magician.title() + ", that was a great trick!")
   print("I can't wait to see your next trick " + magician.title() + '.\n')
   print("I can't wait to see your next trick, {}.\n".format(magician.title()))
print("Thank you, everyone. That was a great magic show!")
print("------------------------------------------------------")