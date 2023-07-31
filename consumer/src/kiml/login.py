from csms.cli.main import login_ApplicationCredential


def login_kiml(id, password) -> bool:
    return login_ApplicationCredential(id, password)


if __name__ == "__main__":
    id = "f45837a32bc0451a9f01ffc7d150913f"
    pw = "uE-8aaEPqUpUjWhvF6zzxnEK8b7GkemrElwopRFAcodSmYlE-WIDo-N8s3oOhsVXuMp1u6fM5COmftg1X2VC2g"
    login_kiml(id, pw)