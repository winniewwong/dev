# template for "Stopwatch: The Game"
http://www.codeskulptor.org/#user38_OzouUFICz996nBb.py

import simplegui

# define global variables
time = 0
attempts = 0
success = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
# A = minutes, BC = seconds, D = tenths of seconds
def format(t):
   # format(0) = 0:00.0 
   # format(11) = 0:01.1 
   # format(321) = 0:32.1 
   # format(613) = 1:01.3
   tenths = t % 10
   seconds = t / 10
   minutes = seconds / 60
   seconds = seconds % 60 
   secondsString = str( seconds )
   if seconds < 10:
      secondsString = "0" + str( seconds )
    
   output = str( minutes ) + ":" + secondsString + "." + str( tenths )
   return output 
  
    
print format(0)
print format(11) 
print format(321) 
print format(613) 

# define helper function format that success / attempts
def formatScore():
    output = str( success ) + "/" + str( attempts )
    return output

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    running = True

def stop():
    # stop the timer
    global running
    global success
    global attempts
    
    # update success and attempts (x/y) if START is previously pressed
    if running == True:
       attempts += 1
    
       # wins if the tenths is 0
       tenths = time % 10
       if tenths == 0:
          success += 1
    
    # stopwatch is stopped    
    running = False
    
def reset():
    # reset the timer and set success/attempts to 0/0
    global running
    global time
    global success
    global attempts
    
    running = False
    time = 0
    success = 0
    attempts = 0

# define event handler for timer with 0.1 sec interval
def tick():
  # update the timer by 0.1 second
  global time
  global running
    
  if running == True:  
     time += 1
   
# define draw handler
def draw(canvas):
    
    # display time in the middle of canvas
    canvas.draw_text( format(time), [100,100], 40, "White")
    
    # display score at the upper right corner
    canvas.draw_text( formatScore(), [240,20], 30, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()

# start timer
timer.start()

# Please remember to review the grading rubric
