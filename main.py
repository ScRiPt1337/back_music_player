import argparse
import os
from clint.textui import puts, colored, indent


def main():
	try:
	    banner = r"""
	    __               __
	   / /_  ____ ______/ /__
	  / __ \/ __ `/ ___/ //_/
	 / /_/ / /_/ / /__/ ,<
	/_.___/\__,_/\___/_/|_|_____
	                     /_____/music player
	                     version : v0.1 (beta)
	        """
	    with indent(4, quote='>>>'):
	        puts(colored.red(banner))
	    parser = argparse.ArgumentParser(
	            description='play background music from your terminal.')
	    parser.add_argument('url', metavar='url', type=str, nargs='+',
	                            help='Youtube url or local_file location')
	    args = parser.parse_args()
	    with indent(4, quote='>>>'):
	        puts(colored.yellow("Playing now => " + args.url[0]))
	    os.system("nohup python3 " +os.path.dirname(os.path.abspath(__file__))+"/player.py " + args.url[0] + " >/dev/null 2>&1 &")
	    with indent(4, quote='>>>'):
	        puts(colored.blue("To stop music press ctrl + shift + #"))
	except Exception as e:
	    print(e)


if __name__ == "__main__":
	main()

