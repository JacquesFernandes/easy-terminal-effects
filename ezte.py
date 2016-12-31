'''
note: use \033 instead of \e for escape
'''
import sys;

effect_dict = {
    "reset all":{
        "code":0,
        "description":"Reset all attributes",
        "tag":"\033[0m"
    },
    "bold":{
        "code":1,
        "description":"Bold",
        "tag":"\033[1m"
    },
    "dim":{
        "code":2,
        "description":"Dim",
        "tag":"\033[2m"
    },
    "underlined":{
        "code":4,
        "description":"Underlined",
        "tag":"\033[4m"
    },
    "invert":{
        "code":7,
        "description":"Inverts the color of the text and background",
        "tag":"\033[7m"
    },
    "hidden":{
        "code":8,
        "description":"Hides text (like with password entry for sudo)",
        "tag":"\033[8m"
    }
    # Continue from here with colors
}

class Effect:
    def __init__(self):
        global effect_dict;
        self.effect_dict = effect_dict;
        self.reset_tag = self.effect_dict["reset all"]["tag"];

    def sample(self,text="test"):
        print("bold("+text+"): "+self.bold(text));

    def bold(self,text):
        tag = self.effect_dict["bold"]["tag"];
        text = tag+text+self.reset_tag;
        return(text);


if __name__ == "__main__":
    ef = Effect();
    ef.sample();
