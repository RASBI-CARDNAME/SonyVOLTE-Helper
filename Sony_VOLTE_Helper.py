#Made By RASBI

#Library
import os
import subprocess
import tkinter as tk
from tkinter import filedialog

#variable
number=''  # menu number variable
KEY='' #key for bootloader unlock
file_path = None #address for flashing boot.img
folder_path = None  #address for EFSTOOLS DIR
VERSION = '1.2.0'

#함수
def Clear_page():
    for i in range(0,20):
        print('\n')
    print('\n')

def Make_line():
    print("--------------------")

def Re_select():
    Make_line()
    print("다시 선택해주세요.")
    Make_line()

def Main_menu():
    Make_line()
    print("1. 리커버리로 재부팅")
    print("2. Fastboot로 재부팅")
    print("3. Fastboot 탈출(#os로 부팅)")
    print("4. 부트로더 언락(#주의)")
    print("5. boot.img 플래시(#주의)")
    print("6. init_boot.img 플래시(#주의)")
    print("7. EfsTools 작업")
    print("8. PDC / QPST 포트 열기")
    print("9. VOLTE 스위치 열기")
    print("10. ADB / FASTBOOT 사용(명령어 직접 입력)")
    print("11. 기기 재부팅")
    print("12. 기타")
    print("13. 종료")
    Make_line()

def open_file_dialog():
    while True:
        Confirm_num = 0; #확인 용 변수
        global file_path #전역 변수로 사용할 거라고 알림.
        
        root = tk.Tk() 
        root.withdraw()  # 기본 창 숨기기

        file_path = filedialog.askopenfilename()  # 파일 선택 창 열기

        if file_path:
            Clear_page()
            
            Make_line()
            print("선택한 파일의 경로:", file_path,"\n")
            Make_line()
            print ("맞으면 1 입력 후 엔터, 다시 선택하려면 0 입력 후 엔터")
            Make_line()
            
            Confirm_num=input()

            if Confirm_num == '0' :#다시 선택
                Clear_page()
                Re_select()
                continue

            elif Confirm_num == '1': #확인
                print("")
                break

            else:
                Clear_page()
                Re_select()
                continue
            
        else: # 파일 미선택 시
            Clear_page()
            Make_line()
            print("파일을 선택하지 않았습니다. 처음으로 돌아갑니다.")
            Make_line()
            print("\n")
            break

def get_folder_path():
    while True:
        Confirm_num = 0; #확인 용 변수
        global folder_path  # 함수 내에서 전역 변수를 사용하겠다고 선언

        root = tk.Tk()
        root.withdraw()  # 기본 창 숨기기

        folder_path = filedialog.askdirectory()  # 폴더 선택 창 열기

        if folder_path:
            Clear_page()
            
            Make_line()
            print("선택한 EFSTOOLS 폴더의 경로:", folder_path,"\n")
            Make_line()
            print ("맞으면 1 입력 후 엔터, 다시 선택하려면 0 입력 후 엔터")
            Make_line()
            
            Confirm_num=input()

            if Confirm_num == '0' :#다시 선택
                Clear_page()
                Re_select()
                continue

            elif Confirm_num == '1': #확인
                print("")
                break

            else:
                Clear_page()
                Re_select()
                continue
            
        else:
            Clear_page()
            Make_line()
            print("폴더를 선택하지 않았습니다. 처음으로 돌아갑니다.")
            Make_line()
            print("\n")
            break

def warning() : # 경고문
    print("-----Sony VOLTE Helper",VERSION,"------")
    print('1. FASTBOOT & ADB 드라이버가 설치되어 있어야 합니다')
    print('2. 이외 각종 드라이버를 설치한 상태로 사용해주세요.')
    print("3. USB 디버그 모드와 oem 잠금 해제를 활성화 해주세요.")
    print('4. 이 프로그램은 ADB / FASTBOOT 명령어를 간단하게 사용할 수 있게 해줍니다.')
    print('5. 사용시 일어나는 문제에 대한 책임은 사용자에게 있습니다.')
    Make_line()
    print('\n')
    input('모두 읽었고 동의하신다면 Enter를 눌러주세요...')
    Clear_page()

warning()

# 메인 코드 구동 부
while True:
    file_path =None #에러 방지용 변수 초기화
    
    print("-----Sony VOLTE Helper",VERSION,"------")
    Main_menu()
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

        os.system('adb devices')
        os.system('adb reboot bootloader')

        Clear_page()
        Make_line()
        print("장치관리자에서 드라이버 확인 후 엔터를 눌러주세요...")
        Make_line()
        input()

        Clear_page()
        Make_line()
        print("오래 걸리니 인내심을 갖고 기다려 주세요...")
        Make_line()
        
        ##언락 수행
        os.system(f'fastboot oem unlock 0x{KEY}')
        os.system('fastboot reboot')
        Clear_page()
            
        Make_line()
        print("부트로더 언락 완료.")
        Make_line()
        print("\n")

    elif number == '5' : #boot.img 플래싱
        Clear_page()
        Make_line()
        print("##경고##")
        Make_line()
        print("1. 부트로더 언락 후 사용해주세요.")
        print("2. 잘못된 파일을 플래싱 하지 않도록 주의해주세요.")
        print("3. 벽돌 대비를 위해 순정 boot.img를 준비해주세요.")
        print("4. 수행하는 명령어는 \"fastboot flash boot_b 및 boot_a\" 입니다.")
        Make_line()
        print('\n')
        input('모두 읽었다면 Enter를 눌러주세요...')

        Clear_page()

        Make_line()
        print("새로 열린 창에서 파일 선택을 해주세요...")
        Make_line()
        
        ##작업 수행 부
        open_file_dialog() # boot 파일 선택

        if file_path == '' :
            continue
        
        os.system('adb devices')
        os.system('adb reboot bootloader')

        Clear_page()
        Make_line()
        print("장치관리자에서 드라이버 확인 후 엔터를 눌러주세요...")
        Make_line()
        input()

        #플래싱 시작
        os.system(f'fastboot flash boot_b "{file_path}"')
        os.system(f'fastboot flash boot_a "{file_path}"')
        os.system('fastboot reboot')

        Clear_page()
            
        Make_line()
        print("플래싱 완료. 기기를 확인해주세요.")
        Make_line()
        print("\n")

    elif number == '6' : #init_boot 플래싱
        Clear_page()
        Make_line()
        print("##경고##")
        Make_line()
        print("1. 부트로더 언락 후 사용해주세요.")
        print("2. 잘못된 파일을 플래싱 하지 않도록 주의해주세요.")
        print("3. 벽돌 대비를 위해 순정 init_boot.img를 준비해주세요.")
        print("4. 수행하는 명령어는 \"fastboot flash init_boot\" 입니다.")
        Make_line()
        print('\n')
        input('모두 읽었다면 Enter를 눌러주세요...')

        Clear_page()

        Make_line()
        print("새로 열린 창에서 파일 선택을 해주세요...")
        Make_line()
        
        ##작업 수행 부
        open_file_dialog() # init_boot 파일 선택

        if file_path == '' :
            continue
        
        os.system('adb devices')
        os.system('adb reboot bootloader')

        Clear_page()
        Make_line()
        print("장치관리자에서 드라이버 확인 후 엔터를 눌러주세요...")
        Make_line()
        input()

        #플래싱 시작
        os.system(f'fastboot flash init_boot "{file_path}"')
        os.system('fastboot reboot')

        Clear_page()
            
        Make_line()
        print("플래싱 완료. 기기를 확인해주세요.")
        Make_line()
        print("\n")
        
    elif number == '7' : #efstool 사용
        Clear_page()
        Make_line()
        print("##경고##")
        Make_line()
        print("1. Magisk 루팅 후 사용해주세요.")
        print("2. 스마트폰에 슈퍼유저 권한 요청이 나오면 허용해주세요.")
        print("3. EFS 파일 넣는 작업(QPST)은 따로 해주셔야 합니다.")
        print("4. 수행하는 명령어는 다음과 같습니다:\n")
        print("setprop persist.usb.eng 1")
        print("EfsTools.exe writeFile -i mcfg_autoselect_by_uim -o /nv/item_files/mcfg/mcfg_autoselect_by_uim")
        print("EfsTools.exe writeFile -i mcfg_autoselect_by_uim -o /nv/item_files/mcfg/mcfg_autoselect_by_uim_Subscription01")
        print("EfsTools.exe writeFile -i mcfg_autoselect_by_uim -o /nv/item_files/mcfg/mcfg_autoselect_by_uim_Subscription02\n")
        Make_line()
        print('\n')
        input('모두 읽었다면 Enter를 눌러주세요...')

        Clear_page()

        ##작업 수행 부 1
        command = ['adb', 'shell']
        input_command = 'su\nsetprop persist.usb.eng 1\n'

        result = subprocess.run(command, text=True, input=input_command, capture_output=True, encoding='utf-8')

        Clear_page()
        Make_line()
        print("1. 장치관리자에서 확인해주시고 기기 안잡히면 USB 재연결 or VOLTE 강좌 참고 해주세요.")
        print("2. 그 다음 퀄컴 드라이버 작업 후 엔터를 눌러주세요...")
        Make_line()
        input()

        Clear_page()
        Make_line()
        print("포트 에러시 아래 링크 참조:")
        print("https://cafe.naver.com/x1smart/590963")
        print("\n모두 읽었다면 Enter를 눌러주세요...")
        Make_line()
        input()

        Clear_page()
        Make_line()
        print("새로 열린 창에서 EfsTools 폴더를 선택해주세요...")
        Make_line()
        
        ##작업 수행 부 2
        get_folder_path()

        if folder_path == '' :
            continue

        current_directory = os.getcwd()
        os.chdir(f'"{folder_path}"')
        os.system('EfsTools.exe writeFile -i mcfg_autoselect_by_uim -o /nv/item_files/mcfg/mcfg_autoselect_by_uim')
        os.system('EfsTools.exe writeFile -i mcfg_autoselect_by_uim -o /nv/item_files/mcfg/mcfg_autoselect_by_uim_Subscription01')
        os.system('EfsTools.exe writeFile -i mcfg_autoselect_by_uim -o /nv/item_files/mcfg/mcfg_autoselect_by_uim_Subscription02')
        os.chdir(f'"{current_directory}"')
        
        Clear_page()
            
        Make_line()
        print("작업 완료.")
        Make_line()
        print("\n")

    elif number == '8' : #PDC / QPST 사용을 위한 포트 개방
        Clear_page()
        Make_line()
        print("##경고##")
        Make_line()
        print("1. Magisk 루팅 후 사용해주세요.")
        print("2. 스마트폰에 슈퍼유저 권한 요청이 나오면 허용해주세요.")
        print("3. PDC / QPST 포트 개방을 해주는 명령어 입니다.")
        print("4. 수행하는 명령어는 다음과 같습니다:")
        print("setprop sys.usb.config diag,serial_cdev,rmnet,adb")
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

    elif number == '9' : #VOLTE 토글 활성화
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

    elif number == '10' : #ADB / FASTBOOT 명령어 직접 입력
        Clear_page()
        Make_line()
        input("ADB를 사용하려면 Enter를 눌러주세요....\n------------------------")
        os.system('cmd.exe')
        Clear_page()

    elif number == '11': #reboot
        print("잠시만 기다려 주세요...")
        os.system('adb devices')
        os.system('adb reboot')
        Clear_page()
        Make_line()
        print("재부팅 완료.")
        Make_line()
        print("\n")

    elif number == '12' : #기타 정보
        Clear_page()
        Make_line()
        print("Made by RASBI")
        print("최종 업데이트: 2024-01-05\n")
        print("V 1.2.0")
        print("업데이트 내용: EFS 툴 사용 기능 추가 / QPST PDC 명령어 수정\n")
        Make_line()
        print("VOLTE 강좌를 제공해 주신 소니 사용자 모임 카페의 앨리자님과 소스케님, 회원분들께 감사의 말씀드립니다.")
        Make_line()
        input("모두 읽었다면 Enter를 눌러주세요...\n--------------------")
        Clear_page()
        
    elif number == '13': #종료
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
