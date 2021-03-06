from django.conf import settings
from django.core.management import call_command


# Where to monkeypatch "lib.crypto.tasks.sign_addons" so it's correctly mocked.
SIGN_ADDONS = 'addons.management.commands.sign_addons.sign_addons'


def test_no_overridden_settings(monkeypatch):
    assert not settings.SIGNING_SERVER
    assert not settings.PRELIMINARY_SIGNING_SERVER

    def no_endpoint(ids, **kwargs):
        assert not settings.SIGNING_SERVER
        assert not settings.PRELIMINARY_SIGNING_SERVER

    monkeypatch.setattr(SIGN_ADDONS, no_endpoint)
    call_command('sign_addons', 123)


def test_override_SIGNING_SERVER_setting(monkeypatch):
    """You can override the SIGNING_SERVER settings."""
    assert not settings.SIGNING_SERVER

    def signing_server(ids, **kwargs):
        assert settings.SIGNING_SERVER == 'http://example.com'

    monkeypatch.setattr(SIGN_ADDONS, signing_server)
    call_command('sign_addons', 123, signing_server='http://example.com')


def test_override_PRELIMINARY_SIGNING_SERVER_setting(monkeypatch):
    """You can override the PRELIMINARY_SIGNING_SERVER settings."""
    assert not settings.PRELIMINARY_SIGNING_SERVER

    def preliminary_signing_server(ids, **kwargs):
        assert settings.PRELIMINARY_SIGNING_SERVER == 'http://example.com'

    monkeypatch.setattr(SIGN_ADDONS, preliminary_signing_server)
    call_command('sign_addons', 123,
                 preliminary_signing_server='http://example.com')


def test_force_signing(monkeypatch):
    """You can force signing an addon even if it's already signed."""
    def not_forced(ids, force):
        assert not force
    monkeypatch.setattr(SIGN_ADDONS, not_forced)
    call_command('sign_addons', 123)

    def is_forced(ids, force):
        assert force
    monkeypatch.setattr(SIGN_ADDONS, is_forced)
    call_command('sign_addons', 123, force=True)
