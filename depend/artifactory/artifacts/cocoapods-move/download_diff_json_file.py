import os
import requests

# 差异文件列表
list_data = ["AILib/AILib.json",
"AIZB/AIZBSDK/AIZBSDK.json",
"AIZB/AIZBSDK/test/AIZBSDK.json",
"AIZB/OMOSDK/Feixun.json",
"AIZB/OMOSDK/OMOSDK.json",
"AIZB/OMOSDK/OMOSDK_test.json",
"AIZB/OMOSDK/Test/OMOSDK.json",
"BaseSDK/EDFileSelector/EDUFileSelector-test.json",
"BaseSDK/EDFileSelector/EDUFileSelector.json",
"BaseSDK/EDUNetworking/EDUNetworking-test.json",
"BaseSDK/EDUNetworking/EDUNetworking.json",
"BaseSDK/RxSwift/RxRelay.json",
"BaseSDK/RxSwift/RxSwift.json",
"CBG/Alamofire/Alamofire.json",
"CBG/Kingfisher/Kingfisher.json",
"CBG/Moya/Moya.json",
"CBG/PLCrashReporter/CrashReporter.json",
"CBG/Reachability.swift/Reachability.json",
"CBG/ZipArchive/ZipArchive.json",
"EDAnalytics/EDAnalytics.json",
"EDAudioRecorder/EDAudioRecorder-test.json",
"EDAudioRecorder/EDAudioRecorder.json",
"EDFoundation/EDFoundation-custom.json",
"EDImagePicker/EDUImagePicker-test.json",
"EDLoginKit/EDLoginKit-test.json",
"EDLoginKit/EDLoginKit.json",
"EDLoginKit/EDOneLoginKit-test.json",
"EDLoginKit/EDOneLoginKit.json",
"EDMessageSDK/EDMessageSDK-test.json",
"EDMessageSDK/EDMessageSDK.json",
"EDMessageSDK/Test/EDMessageSDK.json",
"EDObjectStorage/EDObjectStorage-test.json",
"EDPhotoBrowser/EDUPhotoBrowser-test.json",
"EDPhotoBrowser/EDUPhotoBrowser.json",
"EDProductManager/EDProductManager.json",
"EDUIM/EDUCommunicate/EDMessageSDK.json",
"EDUIM/EDUCommunicate/EDUCommunicate-test.json",
"EDUIM/EDUCommunicate/EDUCommunicate.json",
"EDUIM/EDUCommunicate/Test/EDUCommunicate.json",
"EDUIM/FlyImSDK/FlyImSDK.json",
"EDUIM/FlyImSDK/Test/FlyImSDK.json",
"EDULogStatistics/EDUCrashCollection/EDUCrashCollection-test.json",
"EDULogStatistics/EDUCrashCollection/EDUCrashCollection.json",
"EDULogStatistics/EDUDeviceInfoKit/EDUDeviceInfoKit-test.json",
"EDULogStatistics/EDUDeviceInfoKit/EDUDeviceInfoKit.json",
"EDULogStatistics/EDULogBaseKit/EDULogBaseKit-test.json",
"EDULogStatistics/EDULogBaseKit/EDULogBaseKit.json",
"EDULogStatistics/EDULogReportKit/EDULogReportKit-test.json",
"EDULogStatistics/EDULogReportKit/EDULogReportKit.json",
"EDULogStatistics/EDULogStatisticsKit/EDULogStatisticsKit-test.json",
"EDULogStatistics/EDULogStatisticsKit/EDULogStatisticsKit.json",
"EDUMessageCenter/EDUMessageCenter-test.json",
"EDUMessageCenter/EDUMessageCenter.json",
"EDUMessageCenter/Test/EDUMessageCenter.json",
"KDKTStundentFramework/KDKTStundentFrameWork-xc.json",
"KDKTStundentFramework/axframework/EDAnalytics/EDAnalytics-xc.json",
"MiddleHomework/MiddleHomeworkFoundation/Foundation.json",
"MiddleHomework/MiddleHomeworkFoundation/MiddleHomeworkFoundation.json",
"MiddleHomework/MiddleHomeworkStudent/MiddleHomeworkStudent.json",
"MiddleHomework/MiddleHomeworkTeacther/MiddleHomeworkTeacther.json",
"MiddleHomework/MiddleHomeworkTeacther/Teacther.json",
"PrimaryHomework/Business/Business.json",
"PrimaryHomework/Foundation/Foundation.json",
"PrimaryHomework/StudentBusiness/Student.json",
"PrimaryHomework/TeacherBusiness/Teacher.json",
"SecondaryHomework/TStudyDigitalPen/TStudyDigitalPen.json",
"SocketRocket/SocketRocket.json",
"TXLiteAVSDK_TRTC/TXFFmpeg.json",
"TXLiteAVSDK_TRTC/TXLiteAVSDK_TRTC.json",
"TXLiteAVSDK_TRTC/TXLiteAVSDK_TRTC_ReplayKit.json",
"TXLiteAVSDK_TRTC/TXSoundTouch.json",
"ZTF/RobotPen.json",
"ZTF/XZXTeacherZTF-test.json",
"ZTF/XZXTeacherZTF.json",
"ZTF/XZXTeacherZTF/XZXTeacherZTF-test.json",
"ZTF/XZXTeacherZTF/XZXTeacherZTF.json",
"khfw/DripPay/DripPay.json",
"khfw/HandyJSON/HandyJSON.json",
"khfw/JXBanner/JXBanner.json",
"khfw/JXPageControl/JXPageControl.json",
"khfw/SwiftyJSON/SwiftyJSON.json",
"khfw/TZImagePickerController/TZImagePickerController.json"]


# 下载老私服差异文件
def download_diff_json_file():
    for i in list_data:
        url = "https://artifacts.artifactory.com/cocoapods-private/" + i
        payload = {}
        headers = {'Authorization': 'Basic bGVpZ2FvNjpBS0NwOG5IRHIzQ2lZMnI1VmFwckZuVWVmZ01mckVGaHVZQkVDRVRkazY4Y2dWejhHTTNwWXk1YVVVNzFId1VIRTJFQmpMd29z'}
        response = requests.request("GET", url, headers=headers, data=payload)
        local_path = "static1/" + i
        # 新建目录
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        if response.status_code == 200:
            with open(local_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
                print(f"文件已成功下载到本地：{local_path}")
        else:
            print(f"文件下载失败：{local_path}")


if __name__ == '__main__':
    download_diff_json_file()