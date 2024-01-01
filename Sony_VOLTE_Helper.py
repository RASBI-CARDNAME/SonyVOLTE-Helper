#Library
import os
import subprocess

#variable
number=''  # menu number variable
KEY='' #key for bootloader unlock

#함수
def Clear_page():
    for i in range(0,20):
        print('\n')
    print('\n')

def Make_line():
    print("--------------------")

def Main_menu():
    print("1. 리커버리로 재부팅")
    print("2. Fastboot로 재부팅")
    print("3. Fastboot 탈출(#os로 부팅)")
    print("4. 부트로더 언락(#주의)")
    print("5. EFSTOOL 포트 개방")
    print("6. PDC / QPST 포트 열기")
    print("7. VOLTE 스위치 열기")
    print("8. ADB / FASTBOOT 사용(명령어 직접 입력)")
    print("9. 기타")
    print("10. 종료")

# 경고문
print("-----Sony VOLTE Helper------")
print('1. FASTBOOT & ADB 드라이버가 설치되어있어야 합니다')
print('2. 이외 각종 드라이버를 설치한 상태로 사용해주세요.')
print("3. USB 디버그 모드와 oem 잠금 해제를 활성화 해주세요.")
print('4. 이 프로그램은 ADB / FASTBOOT 명령어를 간단하게 사용할 수 있게 해줍니다.')
print('5. 사용시 일어나는 문제에 대한 책임은 사용자에게 있습니다.')
Make_line()
print('\n')
input('모두 읽었고 동의하신다면 Enter를 눌러주세요...')

Clear_page()

# 메인 코드 구동 부
while True:
    print("-----Sony VOLTE Helper------")
    Make_line()
    Main_menu()
    Make_line()
    number = input("번호 입력 => ")

    if number == '1': #reboot recovery
        print("잠시만 기다려 주세요...")
        os.system('adb devices')
        os.system('adb reboot recovery')
        Clear_page()
        Make_line()
        print("리커버리로 부팅하였습니다.")
        Make_line()
        print("\n")

    elif number == '2': # reboot bootloader
        print("잠시만 기다려 주세요...")
        os.system('adb devices')
        os.system('adb reboot bootloader')
        Clear_page()
        Make_line()
        print("Fastboot로 부팅하였습니다.")
        Make_line()
        print("\n")

    elif number == '3': #fastboot reboot
        print("잠시만 기다려 주세요...")
        os.system('fastboot reboot')
        Clear_page()
        Make_line()
        print("OS로 재부팅하였습니다.")
        Make_line()
        print("\n")
    elif number == '4' : #bootloader unlock
        Clear_page()
        Make_line()
        print("##경고##")
        Make_line()
        print("1. 부트로더 언락 시 휴대폰의 모든 데이터가 초기화 됩니다.")
        print("2. 언락 전 반드시 백업 해주세요.")
        print("3. 초기화로 잃어버린 자료는 다시 복원이 불가능 합니다.")
        Make_line()
        print('\n')
        input('모두 읽었고 동의하신다면 Enter를 눌러주세요...')
        
        ## 확인 1차
        Clear_page()
        input('언락 하려면 Enter를 눌러주세요...')
        
        ## 키 값 입력
        Clear_page()
        KEY=input("발급받은 부트로더 언락 키 입력 후 엔터:")
        
        ##키 확인
        Clear_page()
        print("입력하신 키:"+KEY)
        input('확인 후 Enter를 눌러주세요...')
        
        ## 확인 2차
        Clear_page()
        input('Fastboot MODE 진입 후, 장치관리자 확인 후 Enter를 눌러주세요...')
        
        ##언락 수행
        os.system(f'fastboot oem unlock 0x{KEY}')
        os.system('fastboot reboot')
        Clear_page()
            
        Make_line()
        print("부트로더 언락 완료.")
        Make_line()
        print("\n")

    elif number == '5' : #efstool 사용용 포트 개방
        Clear_page()
        Make_line()
        print("##경고##")
        Make_line()
        print("1. Magisk 루팅 후 사용해주세요.")
        print("2. 스마트폰에 슈퍼유저 권한 요청이 나오면 허용해주세요.")
        print("3. EFStool 포트 개방만 해주는 명령어 입니다.")
        print("4. 수행하는 명령어는 \"setprop persist.usb.eng 1\" 입니다.")
        Make_line()
        print("EfsTools.exe writeFile -i mcfg_autoselect_by_uim -o ~~~ 작업은 직접 해주셔야 합니다!!")
        Make_line()
        print('\n')
        input('모두 읽었다면 Enter를 눌러주세요...')

        Clear_page()

        ##작업 수행 부
        command = ['adb', 'shell']
        input_command = 'su\nsetprop persist.usb.eng 1\n'

        result = subprocess.run(command, text=True, input=input_command, capture_output=True, encoding='utf-8')

        Clear_page()
            
        Make_line()
        print("포트 개방 완료.")
        Make_line()
        print("\n")

    elif number == '6' : #PDC / QPST 사용을 위한 포트 개방
        Clear_page()
        Make_line()
        print("##경고##")
        Make_line()
        print("1. Magisk 루팅 후 사용해주세요.")
        print("2. 스마트폰에 슈퍼유저 권한 요청이 나오면 허용해주세요.")
        print("3. PDC / QPST 포트 개방을 해주는 명령어 입니다.")
        print("4. 수행하는 명령어는 \"setprop sys.usb.config diag, serial_cdev, rmnet, adb\" 입니다.")
        Make_line()
        print('\n')
        input('모두 읽었다면 Enter를 눌러주세요...')

        Clear_page()

        ##작업 수행 부
        command = ['adb', 'shell']
        input_command = 'su\nsetprop sys.usb.config diag,serial_cdev,rmnet,adb\n'

        result = subprocess.run(command, text=True, input=input_command, capture_output=True, encoding='utf-8')

        Clear_page()
            
        Make_line()
        print("포트 개방 완료.")
        Make_line()
        print("\n")

    elif number == '7' : #VOLTE 토글 활성화
        Clear_page()
        Make_line()
        print("##경고##")
        Make_line()
        print("1. Magisk 루팅 후 사용해주세요.")
        print("2. 스마트폰에 슈퍼유저 권한 요청이 나오면 허용해주세요.")
        print("3. VOLTE 토글 버튼을 활성화 하는 명령어 입니다.")
        Make_line()
        print('\n')
        input('모두 읽었다면 Enter를 눌러주세요...')

        Clear_page()

        ##작업 수행 부
        command = ['adb', 'shell']
        input_command = 'su\nsetprop persist.dbg.ims_avail_ovr 1\nsetprop persist.dbg.volte_avail_ovr 1\nsetprop persist.dbg.vt_avail_ovr 1\n'

        result = subprocess.run(command, text=True, input=input_command, capture_output=True, encoding='utf-8')

        Clear_page()
            
        Make_line()
        print("작업 완료.")
        Make_line()
        print("\n")

    elif number == '8' : #ADB / FASTBOOT 명령어 직접 입력
        Clear_page()
        Make_line()
        input("ADB를 사용하려면 Enter를 눌러주세요....\n------------------------")
        os.system('cmd.exe')
        Clear_page()

    elif number == '9' : #기타 정보
        Clear_page()
        Make_line()
        print("Made by RASBI")
        print("최종 업데이트: 2024-01-01")
        print("V 1.0.2")
        print("업데이트 내용: 코드 개선 및 오류 수정\n")
        print("VOLTE 강좌를 제공해 주신 소니 사용자 모임 카페의 앨리자님 및 회원분들께 감사의 말씀드립니다.")
        Make_line()
        print("\n")
        Make_line()
        input("모두 읽었다면 Enter를 눌러주세요...\n--------------------")
        Clear_page()
        
    elif number == '10':
        Clear_page()
        Make_line()
        input("Enter를 눌러주세요....\n--------------------")
        os.system('adb kill-server')
        break  # 루프 종료
    
    else:
        print("\n")
        Clear_page()
        Make_line()
        input("올바른 입력이 아닙니다. Enter를 눌러주세요....\n--------------------")
        Clear_page()
