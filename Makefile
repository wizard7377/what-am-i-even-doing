TAR_NAME := BadNums
ENTRY_FUNC := main
all: $(TAR_NAME) $(TAR_NAME).lua $(TAR_NAME).jar $(TAR_NAME).java $(TAR_NAME).js $(TAR_NAME).py $(TAR_NAME).php $(TAR_NAME).cs $(TAR_NAME).swf
	touch $(TAR_NAME).hx
%.java: %.hx
	haxe --$(ENTRY_FUNC) $^ --java .
%.jar: %.hx
	haxe --$(ENTRY_FUNC) $^ --jvm $@
%: %.hx
	haxe --$(ENTRY_FUNC) $^ --cpp .
%.js: %.hx
	haxe --$(ENTRY_FUNC) $^ --js $@
%.py: %.hx
	haxe --$(ENTRY_FUNC) $^ --python $@
%.lua: %.hx
	haxe --$(ENTRY_FUNC) $^ --lua $@
%.php: %.hx
	haxe --$(ENTRY_FUNC) $^ --php .
%.cs: %.hx
	haxe --$(ENTRY_FUNC) $^ --cs .
%.swf: %.hx
	haxe --$(ENTRY_FUNC) $^ --swf $@
			