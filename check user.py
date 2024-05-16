
#definition user and password
users = {
    'user1' : 'password1',
    'user2' : 'password2',
    'user3' : 'password3'
}
#enter username
username = input('لطفا نام کاربری خود را وارد نمائید:')

#if username was in users , enter your password
if username in users:
    password = input('لطفا رمز عبور خود را وارد نمائید:')

#if password equal users print:welcome...or print:incorrect password, or print:user not found.
    if password == users[username]:
        print(f'خوش آمدید{username}!')
    else:
        print('رمز عبور اشتباه است.')
else:
    print('کاربر پیدا نشد.')