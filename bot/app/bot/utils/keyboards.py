from aiogram.types import InlineKeyboardMarkup as Markup, WebAppInfo
from aiogram.types import InlineKeyboardButton as Button

from app.bot.utils.texts import TextButton


def back(text_button: TextButton) -> Markup:
    return Markup(
        inline_keyboard=[
            [text_button.get_button("back")]
        ]
    )


def main(text_button: TextButton) -> Markup:
    return Markup(
        inline_keyboard=[
            [text_button.get_button("main")]
        ]
    )


def back_main(text_button: TextButton) -> Markup:
    return Markup(
        inline_keyboard=[
            [text_button.get_button("back"), text_button.get_button("main")],
        ]
    )


def source_code(text_button: TextButton) -> Markup:
    url = "https://github.com/tonmendon/ton-subdomain/tree/main/bot"

    return Markup(
        inline_keyboard=[
            [text_button.get_button("source_code", url=url)],
            [text_button.get_button("main")]
        ]
    )


def main_menu(text_button: TextButton, is_testnet: bool) -> Markup:
    tondns_url = "https://dns.ton.org/?testnet=true" if is_testnet else "https://dns.ton.org/"
    getgems_url = (
        "https://testnet.getgems.io/collection/EQDjPtM6QusgMgWfl9kMcG-EALslbTITnKcH8VZK1pnH3UZA"
        if is_testnet else
        "https://getgems.io/collection/EQC3dNlesgVD8YbAazcauIrXBPfiVhMMr5YYk2in0Mtsz0Bz"
    )

    return Markup(
        inline_keyboard=[
            [text_button.get_button("select_domain", switch_inline_query_current_chat=" ")],
            [text_button.get_button("buy_ton_domains", web_app=WebAppInfo(url=tondns_url))],
            [text_button.get_button("buy_on_getgems", web_app=WebAppInfo(url=getgems_url))],
            [text_button.get_button("settings_menu")]
        ]
    )


def settings_menu(text_button: TextButton, is_testnet: bool) -> Markup:
    return Markup(
        inline_keyboard=[
            [text_button.get_button("switch_to_mainnet")
             if is_testnet else
             text_button.get_button("switch_to_testnet")],
            [text_button.get_button("change_language")],
            [text_button.get_button("disconnect_wallet")],
            [text_button.get_button("back")],
        ]
    )


def deploy_and_set(text_button: TextButton) -> Markup:
    return Markup(
        inline_keyboard=[
            [text_button.get_button("deploy_and_set")],
            [text_button.get_button("back")],
        ]
    )


def select_options(text_button: TextButton) -> Markup:
    return Markup(
        inline_keyboard=[
            [text_button.get_button("set_storage")],
            [text_button.get_button("set_wallet")],
            [text_button.get_button("set_site")],
            [text_button.get_button("back"), text_button.get_button("main")],
        ]
    )


def select_language(text_button: TextButton, include_back: bool = False) -> Markup:
    inline_keyboard = [
        [Button(text="🇷🇺 Русский", callback_data="ru"),
         Button(text="🇬🇧 English", callback_data="en")],
    ]
    if include_back:
        inline_keyboard.append([text_button.get_button("back")])
    return Markup(inline_keyboard=inline_keyboard)
