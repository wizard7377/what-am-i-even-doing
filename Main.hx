import haxe.ds.Vector;

class Main {
	static var totalLen = 10;
	static function generateRandom(len:Int = 100) {
		var rVec:Vector<Int> = new Vector(len);
		for (v in 0...len) {
			rVec[v] = Math.round((Math.random() * 100000));
		}
		//trace (rVec);
		return rVec;
	}
	static public function main():Void {
		var i = 0;
		var rVec:Vector<Int> = generateRandom(totalLen);
		trace (rVec);
		while (i < totalLen-1) {
			if (rVec[i] > rVec[i+1]) {
				var tVar = rVec[i];
				rVec[i] = rVec[i+1];
				rVec[i+1] = tVar;
				i--;
			} else {
				i++;
			}
			if (i < 0) i = 0;
		}
		trace(rVec);
	}


	
}
