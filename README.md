# TDK-2022

This is a repository for TDK-2022 competition.

[第 26 屆 TDK 盃全國大專校院創思設計與製作競賽 【自動組】競賽規則](https://tdk.stust.edu.tw/upload/news/files/26th%20TDK%E7%9B%83%E8%87%AA%E5%8B%95%E7%B5%84%E7%AB%B6%E8%B3%BD%E8%A6%8F%E5%89%87.pdf)

## meeting notes

You can find meeting notes here:

[iTron - HackMD](https://hackmd.io/team/iTron-robotics-team?nav=overview)

## Missions

- Alphabet Recognition: use opencv to detect contours

## Node Graph

```mermaid
flowchart TD

dot_recognize -- 丟一個數字 --> main_control
alphabet_recognize -- 丟一個字母 --> main_control
color_detect -- 丟byte --> main_control

distance_from_camera -. 距離或離中間距離 .-> main_control
main_control -- 目前狀態 --> distance_from_camera

navigation -.得到目前位置座標.-> main_control
main_control -- 丟一個geometry --> navigation

navigation -- 丟前進後退等指令 --> motor_control
motor_control -. 得到速度等資訊 .-> navigation
```

- 目前狀態為一個字串，代表需要掃描的東西
  - `"alphabet"`
  - `"basketball"`
  - `"bowling"`
  - `"dot"`
- 距離或離中間距離代表會回傳以下東西
  - 一個距離(數字)
  - 距離代表的意義
    - 物體不在中間，`"attitude adjustment"`
    - 物體在中間，`"distance detect"`

## Flowchart

```mermaid
flowchart TD

id1([A]) --> id2[走到I] --> id3{位置準確嗎} -- yes --> id4[夾三顆籃球]

id3 -- no --> id2

id4 --> id5[走到G] --> id6{位置準確嗎} -- yes --> id7[投籃] --> id8{投完了嗎} -- yes --> id9[走到J]
id6 -- no --> id5
id8 --no--> id5
id9 --> id10{位置準確嗎}
id10 -- yes --> id11[拿保齡球]
id10 -- no --> id9
id11 --> id12[走到H] --> id13{位置準確嗎}
id13 -- yes --> id14[投保齡球]
id13 -- no --> id12
id14 --> id15{投完了嗎}
id15 --yes--> id16([任務結束])
id15 --no-->id12
```
