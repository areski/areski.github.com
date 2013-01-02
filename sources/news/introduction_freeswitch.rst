Introduction to FreeSWITCH
##########################

:date: 2012-12-30 19:00
:author: Areski Belaid
:category: FreeSWITCH


FreeSWITCH is free and open source communications platform that helps to create voice and messaging application. It is licensed under the Mozilla Public License (MPL). The original author is Anthony Minessale and was first announced in January 2006.
it's a very stable, scalable VoIP Softswitch, which offer a lot of flexibility for developers.

If you are a VoIP Enthousiast and only played with Asterisk, I will recommend you to give it a go.

Get Started : http://wiki.freeswitch.org/wiki/Getting_Started_Guide

Install
~~~~~~~
If you want to install FreeSWITCH on an Ubuntu 12.04 TLS without too much pain :
https://github.com/areski/newfies-dialer/blob/master/install/install-freeswitch.sh

Now if you are using CentOS, you can easily install it that way :

a) install the Freeswitch Repo
rpm -Uvh http://files.freeswitch.org/yum/freeswitch-release-1-0.noarch.rpm

b) install the freeswitch files
yum -y install freeswitch-config-vanilla freeswitch-codec-siren freeswitch-codec-passthru-amr freeswitch-application-conference freeswitch-application-db freeswitch-endpoint-dingaling freeswitch-application-enum freeswitch-application-esf freeswitch-application-expr freeswitch-application-fifo freeswitch-asrtts-flite freeswitch-application-fsv freeswitch-codec-passthru-g723_1 freeswitch-codec-passthru-g729 freeswitch-codec-h26x freeswitch-application-hash freeswitch-application-httapi freeswitch-codec-ilbc freeswitch-format-local-stream freeswitch-lua freeswitch-format-native-file freeswitch-lang-de freeswitch-lang-en freeswitch-lang-fr freeswitch-lang-ru freeswitch-format-mod-shout freeswitch-codec-speex freeswitch-spidermonkey freeswitch-format-tone-stream freeswitch-asrtts-tts-commandline freeswitch-application-valet_parking freeswitch-application-voicemail freeswitch-format-shell-stream

Once you have FreeSWITCH installed and running you will want to start making full calls, there is 2 main scenarios that we always want to replicate when we set a box, the first one is to call in, for instance let's a user call VoIP application and the second is to call out, either by doing a raw outbound call from the platform to the PSTN or by allowing a user to call in and then call out to someone in the realworld.

So let's do the seconds approach as it covers both case.

1. Configure SIP phone to call in.

texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto

2. Configure outbound Gateway

texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto


3. Configure a Dialplan to let the user call an extension and call out

texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto texto


You want to go deeper into FreeSWITCH, the wiki is very rich and you might found answer to most of your question.
Sometimes is just more simple to lie back and read a book, so for those that like the paper :
https://www.packtpub.com/freeswitch-1-0-6-build-robust-high-performance-telephony-systems/book


Well that's not too bad, isn't it!
If you have few ideas to improve this article and wants to share some of the issues you met.


/Seeu pronto
