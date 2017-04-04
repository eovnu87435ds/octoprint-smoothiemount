\# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class smoothiemountPlugin(octoprint.plugin.StartupPlugin,
			  octoprint.plugin.TemplatePlugin,
			  octoprint.plugin.SettingsPlugin,
			  octoprint.plugin.AssetPlugin):

    def on_after_startup(self):
        self._logger.info("SmoothieMount Started")

__plugin_implementation__ = smoothiemountPlugin()
__plugin_name__ = "Smoothieboard SD Mount" 
def get_settings_defaults(self):
	return dict(smoothiedevice="/dev/sda1")

def get_template_configs(self):
	return [
		dict(type="settings",custom_bindings=False)
	]

def get_assets(self):
	return dict(
		js=["js/smoothiemount.js"]
	)


