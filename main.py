# import pytorch
import torch
import pyautogui
import pprint
import cv2

def registerAgents():
    print("registering agents...")

    global ag_kayo
    global ag_astra
    global ag_viper
    global ag_omen 
    global ag_killjoy
    global ag_cypher
    global ag_jett 
    global ag_skye 
    global ag_sage 
    global ag_sova 
    global ag_chamber
    global ag_phoenix
    global ag_breach
    global ag_brimstone
    global ag_yoru 
    global ag_raze 
    global ag_reyna

    global agents

    ag_kayo = agentData([[586, 887], [661, 962]], "source/agent/kayo.png")
    ag_astra = agentData([[670, 887], [745, 962]], "source/agent/astra.png")
    ag_viper = agentData([[754, 887], [829, 962]], "source/agent/viper.png")
    ag_omen = agentData([[838, 887], [913, 962]], "source/agent/omen.png")
    ag_killjoy = agentData([[922, 887], [997, 962]], "source/agent/killjoy.png")
    ag_cypher = agentData([[1006, 887], [1081, 962]], "source/agent/cypher.png")
    ag_jett = agentData([[1090, 887], [1165, 962]], "source/agent/jett.png")
    ag_skye = agentData([[1174, 887], [1249, 962]], "source/agent/skye.png")
    ag_sage = agentData([[1258, 887], [1333, 962]], "source/agent/sage.png")
    ag_sova = agentData([[586, 971], [661, 1046]], "source/agent/sova.png")
    ag_chamber = agentData([[670, 971], [745, 1046]], "source/agent/chamber.png")
    ag_phoenix = agentData([[754, 971], [829, 1046]], "source/agent/phoenix.png")
    ag_breach = agentData([[838, 971], [913, 1046]], "source/agent/breach.png")
    ag_brimstone = agentData([[922, 971], [997, 1046]], "source/agent/brimstone.png")
    ag_yoru = agentData([[1006, 971], [1081, 1046]], "source/agent/yoru.png")
    ag_raze = agentData([[1090, 971], [1165, 1046]], "source/agent/raze.png")
    ag_reyna = agentData([[1174, 971], [1249, 1046]], "source/agent/reyna.png")

    # all agent in agents
    agents = [ag_kayo, ag_astra, ag_viper, ag_omen, ag_killjoy, ag_cypher, ag_jett, ag_skye, ag_sage, ag_sova, ag_chamber, ag_phoenix, ag_breach, ag_brimstone, ag_yoru, ag_raze, ag_reyna]


def testrun(model):
    img = cv2.imread("result/images/0.png")
    # color fix
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = model(img)
    result.display(pprint=True)
    result.display(show=True)

def cut():
    # take screenshot
    global screenshot
    screenshot = pyautogui.screenshot(0,0,1920,1080)
    ranges = []
    for agent in agents:
        fix_x, fix_y = [(agent.pos[0][1] - agent.pos[0][0]), (agent.pos[1][1] - agent.pos[1][0])]
        ranges.append((agent.pos[0][0], agent.pos[1][0], fix_x, fix_y))
    
    return ranges


def main():
    print("v-autopicker is starting...")
    print("PyTorch Version:", torch.__version__)
    print("OpenCV Version:", cv2.__version__)
    global model
    model = torch.hub.load("ultralytics/yolov5", "custom", path="model/best.pt")
    model.conf = 0.15

    # test run
    testrun(model)
    regions = cut()


# call main
if __name__ == '__main__':
    main()

class agentData:
    pos = None
    img = None

    def __init__(self, pos, img):
        self.pos = pos
        self.img = img
