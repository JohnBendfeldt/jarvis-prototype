import wx
import wikipedia
import wolframalpha
import pyttsx
import speech_recognition as sr

def say(s):
        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)                                                                                       
        engine.say(s)
        a = engine.runAndWait()   

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(500, 120),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Jarvis Jr. a Python Digital Assistant. How can I help you? Press Enter to speak to me, or type in a query.")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(450,45))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        say("Welcome, how may I help you?")
    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        if input == '':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recogniton service; {0}".format(e))
        else:
            try:
                #wolframalpha
                app_id = "Q3A4WW-4Y2WTGEXP3"
                client = wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text
                print(answer)
                say("The answer is " + answer)            
            except:
                #wikipedia
                print(wikipedia.summary(input))
                say("Sorry for the wait, sir")    

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
app.MainLoop()
