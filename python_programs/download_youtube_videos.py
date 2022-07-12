from pytube import YouTube

links = ['https://youtu.be/5ZiSivp9TUc','https://youtu.be/93hRvFHyhcM','https://youtu.be/xT52Eh7E9-o',
         'https://youtu.be/WX4cuGSa4yE','https://youtu.be/gWELu5OuO2Q','https://youtu.be/uXEZprIKrEo',
         'https://youtu.be/5IHp3Zo6nmQ','https://youtu.be/0trwPTIhefE','https://youtu.be/P8n7TOoA-B0',
         'https://youtu.be/MS544iwubdc','https://youtu.be/fzpcC-CED2I','https://youtu.be/BzqukMvD5M4',
         'https://youtu.be/WpP0UsuD30E','https://youtu.be/zKkDVZrkaoM','https://youtu.be/pITzjm2Tzbw',
         'https://youtu.be/3z4b5WfwoeY','https://youtu.be/NaFjWEn2AME','https://youtu.be/C2Iw0rhrtFk',
        'https://youtu.be/hb2RW8GM-28','https://youtu.be/ZLa8xwIRHUc','https://youtu.be/ezOTWTL6ulI',
        'https://youtu.be/jzOwCZv6pok','https://youtu.be/djE0nGysCXs','https://youtu.be/4k1p8qOrD9Y',
        'https://youtu.be/aYXy5pCA1QQ','https://youtu.be/GX0gPnrBFRs','https://youtu.be/isolOlmS2Q0',
        'https://youtu.be/5-KDGMXvZrM','https://youtu.be/SsiRuGB0oQc','https://youtu.be/jIZhi4T6S-U',
        'https://youtu.be/mGjaNYkuE6M','https://youtu.be/_q0HiGEyNIw','https://youtu.be/QpFLeSCKBac',
         'https://youtu.be/Tkiizn-ZYHI','https://youtu.be/EAVYw__si2Q','https://youtu.be/bIcnCl7QrKw',
         'https://youtu.be/RN_JgWYrjps','https://youtu.be/If0yuUfXNXc','https://youtu.be/OsBWEIiFmtE',
         'https://youtu.be/WSs25QtAZZM','https://youtu.be/PX0kbqvRd9o','https://youtu.be/Qf_dxnaJJa0',
         'https://youtu.be/qgSuptwfP7k','https://youtu.be/xCVPcQvcDRA','https://youtu.be/9nz-TTXI64s',
         'https://youtu.be/ex-08FJPwTA','https://youtu.be/pbzeosGRKkU','https://youtu.be/fnQPOdC5poA',
         'https://youtu.be/mIiAoDWuqh8','https://youtu.be/mfNqv2gkXgc','https://youtu.be/qFc_S_k0DwE',
         'https://youtu.be/Qlotok-5NN0','https://youtu.be/wo7xHPSxOfg','https://youtu.be/AEYBqhr9Nb0',
         'https://youtu.be/N5y9cwjvk0Y','https://youtu.be/difl73WCXpE','https://youtu.be/0qcXjwnjdUw',
         'https://youtu.be/yS2jMTqZ7E0','https://youtu.be/WUilNN0PTds','https://youtu.be/rEMQaK1YrZM',
         'https://youtu.be/8hwUDzUt6hs','https://youtu.be/90aZJpHT0NI','https://youtu.be/Lils_PTC-74',
         'https://youtu.be/pLhae6Z9xGY','https://youtu.be/MhDHL4iJeXk','https://youtu.be/TmuKL1i6OuU',
         'https://youtu.be/eEW3LXZH-jQ','https://youtu.be/02m1aio7rQo','https://youtu.be/4auC9aME4-8',
         'https://youtu.be/foFunTQOd1U','https://youtu.be/afKiMkaJKeE','https://youtu.be/9ZOC5z1YvCc',
         'https://youtu.be/Qku8BrBY6c0','https://youtu.be/581Y_CxCwQw','https://youtu.be/i3zbtbIflns',
         'https://youtu.be/CfAbSSHnhvo','https://youtu.be/4g8dkSuJqpc','https://youtu.be/e2oe_yUcSSQ',
         'https://youtu.be/H_1bxc59-dg','https://youtu.be/-7PAK-6GF5s','https://youtu.be/i8wAvAKHpIU',
         'https://youtu.be/6NM36fa_TMw','https://youtu.be/7q6sfoWBBRc','https://youtu.be/g1PstLMVKbk',
         'https://youtu.be/uEOmNbslG5k','https://youtu.be/5Zt3KryH_co','https://youtu.be/1SQaYo1fP0Q',
         'https://youtu.be/XOiOb9Nkx4I','https://youtu.be/lvbSWxROpc8','https://youtu.be/GLdHw3T2kZM',
         'https://youtu.be/s1_Xl67XUag','https://youtu.be/R0gHtCz4Neg','https://youtu.be/zVEGaD7muHw',
         'https://youtu.be/M8f_vhagcuc','https://youtu.be/Z0ZyLl9ugig','https://youtu.be/vDzWfbbent8',
         'https://youtu.be/RngCdYsw9Hw','https://youtu.be/IX7wivtbQAU','https://youtu.be/wgD59xdTiVM',
         'https://youtu.be/QoDstux-bOc','https://youtu.be/t7F4feaon9Q','https://youtu.be/meeaihOwlB8',
         'https://youtu.be/o2xtU2gfzUg','https://youtu.be/hwECM7AiNss','https://youtu.be/Yj2SGG9jlcw',
         'https://youtu.be/TLyXpIIT6Ck','https://youtu.be/AkGib4Grqvg','https://youtu.be/pJ3Q51AeFyU',
         'https://youtu.be/ck7PiIaSkYU','https://youtu.be/baprxefdKR4','https://youtu.be/VbE8rYLUiBs',
         'https://youtu.be/f9334mGLxbI','https://youtu.be/bnQlpnO-XZo','https://youtu.be/_D44GZPlxG8',
         'https://youtu.be/pH1Z2FZtbgY','https://youtu.be/o0H9Dj-jh3M','https://youtu.be/ZAMS4fKkgSM',
         'https://youtu.be/NlsnENk8PhA','https://youtu.be/ZuWocbRNcxs','https://youtu.be/niIibCxLr-M',
         'https://youtu.be/c3SEfWdEibY','https://youtu.be/tSqkQOQSuiI','https://youtu.be/7npSJHMVIO8','https://youtu.be/euJXkYvOUoM']
print(len(links))
j=1
for i in links:
    video = YouTube(i)
    if video.streams.filter(file_extension='mp4').get_by_itag(137) or video.streams.filter(file_extension='mp4').get_by_itag(299):
        video_streams = video.streams.filter(file_extension='mp4').get_by_itag(137) or video.streams.filter(file_extension='mp4').get_by_itag(299)
        print(f'{j} video downloading')
        video_streams.download(output_path = 'C:\\Users\shaik firoz babu\\Desktop\\desktop files\\shorts in other social media platforms\\allvideos_youtube_shorts')
        print(f'{j} video downloaded')
        print(f'{j+1} video downloading')
        j+=1
print('All videos downloaded')
