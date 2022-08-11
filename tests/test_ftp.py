from __future__ import annotations

from ftplib import FTP

from pytest_localftpserver.servers import FunctionalityWrapper


def test_ftp(ftpserver: FunctionalityWrapper) -> None:
    ftp = FTP()
    ftp.connect(host="localhost", port=31175)
    ftp.login(user="user", passwd="pass")

    with open(__file__, "rb") as file:
        ftp.storbinary("STOR test_file.py", file)

    result = ftp.retrlines("LIST")
    assert result == "226 Transfer complete."

    ftp.close()
