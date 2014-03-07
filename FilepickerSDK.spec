Pod::Spec.new do |s|
  s.name         = "FilepickerSDK"
  s.version      = "2.6.3"
  s.summary      = "FPPicker.framework is the Filepicker.io iOS famework."
  s.homepage     = "https://developers.filepicker.io/docs/ios/"
  s.screenshots  = "https://github.com/Filepicker/ios/raw/master/Documenation%20Files/filepicker_ios.png"
  s.license      = { :type => 'MIT', :file => 'license.txt' }

  s.author       = { "Liyan Chang" => "liyan@filepicker.io" }

  s.source       = {
    :git => 'https://github.com/pingwinator/ios-picker.git',
  }

  s.platform     = :ios

  s.source_files = FileList['FPPicker/*.{h,m}'].exclude(/nonarc/)
  s.frameworks   = 'AssetsLibrary', 'QuartzCore', 'CoreGraphics', 'MobileCoreServices', 'Foundation', 'CoreFoundation'
  
  s.requires_arc = true

  s.resource = "dist/FPPicker.bundle"

  s.subspec 'no-arc' do |sp|
    sp.source_files = 'FPPicker/nonarc/*.{h,m}'
    sp.requires_arc = false
  end
end
