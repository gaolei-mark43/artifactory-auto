#!/usr/bin/python
import subprocess
import time

start_time = time.time()

dir_list = ["finger-library","expression-editor","@qzk/qzk-activity","speechUtil","@qzk/qzk-preview","kityminder-core","@bjke/ts-build","@bjke/webpack-js","@bjke/webpack-ts","@bjke/webpack-iflytek","@bjke/webpack-asar","@bjke/webpack-glsl","gatsby-theme-antv","zhkt-base","@zhkt/ffi","@zhkt/ref","@zhkt/sqlite3","@zhkt/sequelize","@zhkt/ref-struct","@zhkt/webpack","@zhkt/handwriting-recognize","@zhkt/node-expat","@zhkt/speech-util","@qzk/gm","@bjke/webpack-vue","@zhkt/downloadupload","@zhkt/rc-cloud","@zhkt/rc-xiaoben","@zhkt/rc-xuekewang","@zhkt/rc-preview","@zhkt/yunpan","@zhkt/beikeben","@zhkt/bookpopup","@zhkt/ref-array","@fly-voter/gm","@fly-voter/import-fly-voter-asar","@fly-voter/makechinesepy","@fly-voter/flyvoter-ui","@fly-voter/flywfs.js","@zhkt/cli-service","@zhkt/cli","@zhkt/learning-report","@zhkt/nan-ks-addon","@zhkt/rc-anhui","@zhkt/rc-area","@zhkt/nan-win32-addon","@iflytek/sentry","wx-cookies","@ebg/formula-keyboard","@zhkt/ApiGatewayJSSDK","import-doublet-fly-voter-asar","@zhkt/mutex-addon","@zhkt/mqserver-addon","@zhkt-tool/zhkt-link","@illusion4ng/eslint-config-vue","@zhkt/vue-zhkt-permission","@zhkt/mqclientsdk","@bubbty/animation","@bubbty/elements","@bubbty/settings","@bubbty/ui","@bubbty/core","@zhkt/importflyvoter","@bubbty/editor","@bubbty/slide","@bubbty/player","generateSlides","@xfkj/utils","@xfkj/fcui","@xfkj/fcui-vite","@xfkj/vite-plugin-md","@bubbty/widget","@zhkt/detect-mpv","@qzk/qzk-mycourses","@zhkt/component_teaching","@zhkt/ai_engine","solid_geometry","@zhkt/zhkt-util","main","resource","@flyvoter/interact-ui","@bubbty/bubbtyjs"]

for dir in dir_list:
    command = 'jf rt u "{}/**" npm_test'.format(dir)
    print(command)
    subprocess.call(command, shell=True)

end_time = time.time()
total_time = end_time - start_time

hours, remainder = divmod(total_time, 3600)
minutes, seconds = divmod(remainder, 60)

print('Total running time: {}h {}min {}s'.format(int(hours), int(minutes), int(seconds)))

