#!/bin/bash
RESET=`/usr/local/sbin/factory`
echo "content-type: text/plain"
echo
echo  "Hard reset to default settings" 
echo  "$RESET"
print <<END1;
<HTML>
    <HEAD>
END1

if ($redirect){
    print '<meta http-equiv="refresh" content="1;url=http://yahoo.com">';
}

print <<END2;
        <TITLE> </TITLE>
    </HEAD>
    <body>
        <form NAME="login"  METHOD="POST">
            <input type="hidden" name="submit" value="Submit">
            <TABLE align="center" bgcolor=#B0C4DE>
                <TR>
                    <TD> Enter The Password And Click Login</TD>
                </TR>
                <TR></TR>
                <TR></TR>
                <TR></TR>
                <TR></TR>
                <TR></TR>
                <TR>
                    <TD><b>PASSWORD</b> :<input type="password" name="Password" size="20" maxlength="15" /></TD>
                </TR>
                <TR></TR>
                <TR></TR>
                <TR></TR>
                <TR></TR>
                <TR></TR>
                <TR>
                <TR>
                    <TD align="center" colspan="2">
                        <input type="submit" name="Login" value="Login">
                        <input type="reset" name="submit" value="Cancel">
                    </TD>
                </TR>
            </TABLE>
        </FORM>
   </BODY>
</HTML>
END2
