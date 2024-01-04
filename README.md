# SonyVOLTE-Helper
## 개요
엑스페리아 기종의 VOLTE 패치 커맨드를 간단하게 입력해주는 프로그램 입니다
## 기능   
1. 리커버리로 부팅
2. FASTBOOT로 부팅
3. FASTBOOT 탈출
4. 부트로더 언락   
5. boot.img 플래싱
6. 기기 재시작

7. EFSTOOL 포트 개방 (setprop persist.usb.eng 1 명령어)
8. PDC / QPST 포트 개방 (setprop sys.usb.config diag,serial_cdev, rmnet, adb 명령어)
9. VOLTE 스위치 활성화 (아래 명령어)
ㄴsetprop persist.dbg.ims_avail_ovr 1
ㄴsetprop persist.dbg.volte_avail_ovr 1
ㄴsetprop persist.dbg.vt_avail_ovr 1

10. ADB / FASTBOOT 명령어 직접 입력
11. ADB kill server로 완전 종료 지원
## 지원 기종  
QPST 작업을 하는 엑스페리아 1 마크1 / 5마크 1 이후 기종
</br>
이전 기종에 대해서는 명령어 작동 보증이 없습니다.
## Thanks to
프로그램 완성에 도움을 주신 앨리자님과 소니 사용자모임 회원분들께 감사 말씀 드립니다.
