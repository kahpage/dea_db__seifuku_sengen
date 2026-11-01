# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = 1  # ==== seifuku_sengen1 ====
    if i not in disabled_events:
        event_name = f"seifuku_sengen{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_ttc08.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20170628131625/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="TTC８＆制服宣言チラシ絵　ふじの芳夏 様（PERFECT SEA）",
            ),
            Medium(
                "01_161002_layout.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20170309032500/http://ttc.ninja-web.net/ttc08-list.htm",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 イベントホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20170628131625/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["制服宣言", "Seifuku Sengen", "制服宣言1", "Seifuku Sengen 1"],
            dates="2016.10.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20160301223834/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20170309032500/http://ttc.ninja-web.net/ttc08-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Part of the ツインテールカーニバル８＆制服宣言 joint venue, also simultaneous with VOCALOID PARADISE 11, ゆかりPARADISE, モジュールPARADISE２, カゲロウパラダイス２ and ずんだぱ～てぃ３（み!）",
            # comments=None,
            last_edited="2026.11.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== seifuku_sengen2 ====
    if i not in disabled_events:
        event_name = f"seifuku_sengen{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_ttc09.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="TTC９・制服宣言２・絶対ニーソ・百合乙女の楽園 チラシ絵 朝倉亮 様（水無月亭）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 白鳥ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["制服宣言2", "Seifuku Sengen 2"],
            dates="2018.11.04",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20190612181841/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
                Source(
                    "Joint venue: https://web.archive.org/web/20190408141004/http://ttc.ninja-web.net/nagoya-doujin-fes/circle_list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Part of the 名古屋熱田同人祭2018秋 (ツインテールカーニバル9, 制服宣言2, 絶対ニーソ and 百合乙女の楽園) joint venue, which also features 艦隊ぱれーど２, 御城まつり, 月下の祭典Returns, アズールフェスタ, BanG Dreamer's Party! in 名古屋 and 魔法少女本作製計画SP",
            # comments=None,
            last_edited="2026.11.01",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== seifuku_sengen3 ====
    if i not in disabled_events:
        event_name = f"seifuku_sengen{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_ttc10.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20200628221937/http://ttc.ninja-web.net/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="メインビジュアル（チラシ絵）　ササキシオリ 様（しおさいと。）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1708859, 136.8837218),
                address="4-chōme-4-38 Meieki, Nakamura Ward, Nagoya, Aichi 450-0002, Japan",
                description="名古屋企業福祉会館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20200628221937/http://ttc.ninja-web.net/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://streetviewpixels-pa.googleapis.com/v1/thumbnail?output=thumbnail&cb_client=maps_sv.tactile.gps&panoid=plEI7dd2WTUE58egOJKX3g&w=1177&h=1300&yaw=170&pitch=-40",
                url="https://maps.app.goo.gl/6F2N7Dtys66bRMQQ9",
            ),
        ]
        event = Event(
            aliases=["制服宣言3", "Seifuku Sengen 3"],
            dates="2020.08.23 → CANCELLED",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20200628221937/http://ttc.ninja-web.net/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Cancelled: https://x.com/ttc_doujin/status/1290279699688505346",
                    (RT.Reliable, OT.OfficialExt),
                ),
            ],
            locations=locations,
            description="Simultaneous with ツインテールカーニバル10, Augustic Memories 2 and ゆずソフトパーティー",
            comments="As it was cancelled before any circle participation was confirmed, no circles list exists.",
            last_edited="2026.11.01",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== seifuku_sengen ====
    # if i not in disabled_events:
    #     event_name = f"seifuku_sengen{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=,
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.11.01",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = [
        "http://ttc.ninja-web.net/",
    ]

    event_group = EventGroup(
        aliases=[
            "制服宣言",
            "Seifuku Sengen",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            Source(
                "Alias transliteration: guess from onyomi",
                (ReliabilityTypes.Guess, OriginTypes.Unsourced),
            ),
        ],
        comments=None,
        description=None,
        last_edited="2026.11.01",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
