function ajaxCall() {
    const logPrefix = '[jupyter-cogram-sources-loader]';
    let out = {};
    $.ajax({
        url: '/apiInfo',
        dataType: 'json',
        timeout: 5000,
        async: false,
        success: (data) => out = data,
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(logPrefix, jqXHR, textStatus, errorThrown)
        }
    })
    return out;
}

function getCogramCDNPath() {
    const logPrefix = '[jupyter-cogram-sources-loader]';
    console.log(logPrefix, "Fetching Cogram JS sources CDN URL")
    let cdn_url = 'https://storage.googleapis.com/cogram-public/jupyter-cogram/latest/cogram_main.min.js';
    console.log(logPrefix, "Default URL is", cdn_url)
    let data = ajaxCall();
    const js_sources = data?.jupyter_cogram?.js_sources ?? []
    if (js_sources.length > 0) {
        let url = js_sources[0]?.source_url
        if (url && url !== cdn_url) {
            console.log(logPrefix, "Updated JS sources CDN URL to", url)
            url = url.replace('https:', '').replace('http:', '')
            console.log(logPrefix, "Shortened JS URL to", url)
            cdn_url = url;
        } else {
            console.log(logPrefix, "Sticking to default JS sources URL")
        }
    }
    console.log(logPrefix, "Loading Cogram JS sources from", cdn_url)
    return cdn_url;
}

define([
    getCogramCDNPath()
], function (
    cogram_module
) {
    "use strict";

    return {
        load_jupyter_extension: cogram_module.load_jupyter_extension,
        load_ipython_extension: cogram_module.load_jupyter_extension
    }
});
