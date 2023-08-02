from csms.sdk import login_idpw
from csms.sdk.core.configuration import Config, load_config


def create_ac_config(id, password) -> bool:
    try:
        Config().set(user_ac_id=id)
        Config().set(user_ac_secret=password)
        Config().set(user_token="")
        Config().set(user_id="")
        Config().set(host="https://api.ml.kakaoicloud-kr-gov.com")
        return True
    except Exception as e:
        Exception(f"failed to set application credential ({id}) / {e}")
        return False


def login_ApplicationCredential(id, password) -> bool:
    try:
        resp = login_idpw("ApplicationCredential", id, password)
        if resp is None:
            print("failed to login.")
            return False
        if not hasattr(resp, "X-User-Token"):
            print("invalid user.")
            return False
    except Exception:
        return False

    Config().set(user_token=resp["X-User-Token"])
    Config().set(user_id=id)
    Config().set(domain_id=resp["domainId"])
    Config().set(project_id=resp["projectId"])
    print(f"'{resp['user']['id']}' is logged in KiML.")
    return True


def login_kiml(id, password) -> bool:
    _id = Config.get().config.user_ac_id
    secret = Config.get().config.user_ac_secret

    if login_ApplicationCredential(_id, secret):
        pass
    else:
        _ = create_ac_config(id, password)

        config = load_config()
        _id = config.user_ac_id
        secret = config.user_ac_secret

        if login_ApplicationCredential(_id, secret):
            pass
        else:
            Exception("invalid access key. Please check again.\n")  # noqa: E501, E261

    return True
