import cv2
class openpose:
    def __init__(self,image):        
        # 관절 번호: 머리는 0, 목은 1 등등
        self.BODY_PARTS = {"Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                    "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                    "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
                    "Background": 15}
        
        # 관절들을 선으로 이을 때 쌍이 되는 것들
        self.POSE_PAIRS = [["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                    ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                    ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                    ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"]]
        
        # 훈련된 network 세팅
        self.protoFile = "pose_deploy_linevec_faster_4_stages.prototxt"
        self.weightsFile = "pose_iter_160000.caffemodel"
        self.net = cv2.dnn.readNetFromCaffe(self.protoFile, self.weightsFile)
        self.image=image
        
        # 테스트 이미지에서 height, width, color 정보 파악
        self.imageHeight, self.imageWidth, self.imageColor = image.shape
 
        # 테스트 이미지를 network에 넣기 위해 전처리
        self.inpBlob = cv2.dnn.blobFromImage(self.image, 1.0 / 255, (self.imageWidth, self.imageHeight), (0, 0, 0), swapRB=False, crop=False)
        
        # 테스트 이미지를 network에 넣어줌
        self.net.setInput(self.inpBlob)
        
        # 결과 받아오기
        self.output = self.net.forward()
        
        self.H = self.output.shape[2]
        self.W = self.output.shape[3]

    def Output(self):
        # 검출된 관절 포인트를 테스트 이미지에 그려주기
        points = []
        for i in range(0, 15):
            # 해당 관절 신뢰도 얻기
            probMap = self.output[0, i, :, :]
        
            # global 최대값 찾기
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        
            # 원래 이미지에 맞게 점 위치 변경
            x = (self.imageWidth * point[0]) / self.W
            y = (self.imageHeight * point[1]) / self.H
        
            # 키포인트 검출한 결과가 0.1보다 크면(검출한곳이 위 BODY_PARTS랑 맞는 부위면) points에 추가, 검출했는데 부위가 없으면 None으로
            if prob > 0.1:
                # cv2.circle(self.image, (int(x), int(y)), 3, (0, 255, 255), thickness=-1,
                #         lineType=cv2.FILLED)  # circle(그릴곳, 원의 중심, 반지름, 색)
                # cv2.putText(self.image, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1,
                #             lineType=cv2.LINE_AA)
                points.append((int(x), int(y)))
            else:
                points.append(None)
        return points
        # return self.image
        # cv2.imshow("Output-Keypoints", self.image)
        # cv2.waitKey(0)

if __name__=="__main__":
    img=cv2.imread('./nodejs/12.jpg')
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    net=openpose(img)
    print(net.Output())
# # 관절들을 선으로 연결해주기
# for pair in POSE_PAIRS:
#     partA = pair[0]  # Head
#     partA = BODY_PARTS[partA]  # 0
#     partB = pair[1]  # Neck
#     partB = BODY_PARTS[partB]  # 1
 
#     # print(partA," 와 ", partB, " 연결\n")
#     if points[partA] and points[partB]:
#         cv2.line(image, points[partA], points[partB], (255, 0, 0), 2)
 
# cv2.imshow("Output-Keypoints-with-Lines", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
