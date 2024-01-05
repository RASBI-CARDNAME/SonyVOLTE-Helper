# SonyVOLTE-Helper
## 개요
엑스페리아 기종의 VOLTE 패치 커맨드를 간단하게 입력해주는 프로그램 입니다
## 기능   
리커버리로 부팅

FASTBOOT로 부팅

FASTBOOT 탈출

부트로더 언락

boot.img 플래싱 (fastboot flash boot_b /boot_a)

기기 재시작 (adb reboot)


EFSTOOL 커맨드 (아래 명령어)

ㄴsetprop persist.usb.eng 1

ㄴEfsTools.exe writeFile -i mcfg_autoselect_by_uim -o /nv/item_files/mcfg/mcfg_autoselect_by_uim

ㄴEfsTools.exe writeFile -i mcfg_autoselect_by_uim -o /nv/item_files/mcfg/mcfg_autoselect_by_uim_Subscription01

ㄴEfsTools.exe writeFile -i mcfg_autoselect_by_uim -o /nv/item_files/mcfg/mcfg_autoselect_by_uim_Subscription02

PDC / QPST 포트 개방 (setprop sys.usb.config diag,serial_cdev,rmnet,adb 명령어)

VOLTE 스위치 활성화 (아래 명령어)

ㄴsetprop persist.dbg.ims_avail_ovr 1

ㄴsetprop persist.dbg.volte_avail_ovr 1

ㄴsetprop persist.dbg.vt_avail_ovr 1

ADB / FASTBOOT 명령어 직접 입력

ADB kill server로 완전 종료 지원
## 지원 기종  
QPST 작업을 하는 엑스페리아 기종

포트 개방 등의 명령어는 기기 os 버전에 따라 동작하지 않을 수 있습니다.
## Thanks to
프로그램 완성에 도움을 주신 앨리자님과 소스케님, 소니 사용자모임 회원분들께 감사 말씀 드립니다.
