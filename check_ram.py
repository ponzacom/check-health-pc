#!/usr/bin/env python3
"""
RAM Health Check Script
Monitors RAM usage and provides health status
"""

import psutil
import sys


def get_ram_info():
    """Get RAM usage information"""
    memory = psutil.virtual_memory()
    return {
        'total': memory.total / (1024 ** 3),  # Convert to GB
        'available': memory.available / (1024 ** 3),
        'used': memory.used / (1024 ** 3),
        'percent': memory.percent
    }


def check_ram_health(percent_used):
    """Determine RAM health status based on usage percentage"""
    if percent_used < 60:
        return "HEALTHY", "RAM usage is normal"
    elif percent_used < 80:
        return "WARNING", "RAM usage is elevated"
    else:
        return "CRITICAL", "RAM usage is critically high"


def main():
    """Main function to check and display RAM health"""
    print("=" * 50)
    print("RAM Health Check")
    print("=" * 50)
    
    # Get RAM information
    ram_info = get_ram_info()
    
    # Display RAM statistics
    print(f"\nTotal RAM: {ram_info['total']:.2f} GB")
    print(f"Used RAM: {ram_info['used']:.2f} GB")
    print(f"Available RAM: {ram_info['available']:.2f} GB")
    print(f"Usage: {ram_info['percent']:.1f}%")
    
    # Check health status
    status, message = check_ram_health(ram_info['percent'])
    
    print(f"\nStatus: {status}")
    print(f"Message: {message}")
    print("=" * 50)
    
    # Return exit code based on status
    if status == "CRITICAL":
        return 2
    elif status == "WARNING":
        return 1
    else:
        return 0


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
